from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Desk, Reservation, OurOffer, ContactForm, ServiceTerm, MainPage
from .forms import ReservationForm
from register.forms import RegisterForm
from django.contrib import messages
from .tasks import send_confirmation_email
from .tasks import send_cancellation_email
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import login
import logging

logger = logging.getLogger(__name__)

def desk_list(request):
    desks = Desk.objects.filter(status="czynne")
    return render(request, 'coapp/desk_list.html', {'desks': desks})

def reserve_desk(request, desk_id):
    if not request.user.is_authenticated:
        return redirect('not_logged_in')

    desk = get_object_or_404(Desk, id=desk_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            total_days = (end_date - start_date).days + 1
            total_cost = desk.price * total_days

            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.desk = desk
            reservation.total_cost = total_cost
            reservation.save()

            desk.status = 'zajęte'
            desk.save()

            # Wyślij e-mail z potwierdzeniem rezerwacji
            send_confirmation_email.delay(reservation.id, request.user.email)
            return redirect('reservation_confirmation', reservation_id=reservation.id)
    else:
        form = ReservationForm(initial={'desk': desk})

    return render(request, 'coapp/reservation_form.html', {'form': form, 'desk': desk})

@login_required
def reservation_confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'coapp/reservation_confirmation.html', {
        'reservation': reservation,
        'desk': reservation.desk,
        'start_date': reservation.start_date,
        'end_date': reservation.end_date,
        'total_cost': reservation.total_cost
    })

@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'coapp/user_reservations.html', {'reservations': reservations})

@login_required
def cancel_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id, user=request.user)
        desk = reservation.desk
        desk.status = 'czynne'
        desk.save()

        # Wyślij e-mail z potwierdzeniem anulowania rezerwacji przed usunięciem rezerwacji
        send_cancellation_email.delay(
            reservation.id,
            request.user.email,
            reservation.desk.stock_number,
            reservation.start_date,
            reservation.end_date,
            reservation.total_cost
        )
        reservation.delete()
        messages.success(request, 'Rezerwacja została anulowana.')
        logger.info(f'Rezerwacja {reservation.id} anulowana przez użytkownika {request.user.email}')
    except Reservation.DoesNotExist:
        messages.error(request, 'Nie znaleziono rezerwacji.')
        logger.error(f'Nie znaleziono rezerwacji {reservation_id} dla użytkownika {request.user.email}')
    return render(request, 'coapp/cancel_confirmation.html')


@login_required
def confirm_cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            return redirect('cancel_reservation', reservation_id=reservation_id)
        else:
            return redirect('user_reservations')

    return render(request, 'coapp/confirm_cancel_reservation.html', {'reservation': reservation})

def home(request):
    return render(request, "coapp/home.html", {})
def mainpage(request):
    mainpages = MainPage.objects.all()
    return render(request, 'coapp/home.html', {'mainpages': mainpages})

def offer(request):
    offers = OurOffer.objects.all()
    return render(request, 'coapp/offer.html', {'offers': offers})

def term(request):
    terms = ServiceTerm.objects.all()
    return render(request, 'coapp/terms.html', {'terms': terms})

def contact(request):
    contact_fields = ContactForm.objects.all()
    return render(request, 'coapp/contact.html', {'contact_fields': contact_fields})

class MyLoginView(LoginView):
    template_name = 'coapp/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def not_logged_in(request):
    return render(request, 'coapp/not_logged_in.html')
