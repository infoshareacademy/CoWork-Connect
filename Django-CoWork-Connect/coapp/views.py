from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Desk, Reservation
from .forms import ReservationForm
from django.contrib import messages


@login_required
def desk_list(request):
    desks = Desk.objects.filter(status="czynne")  # lub inne odpowiednie zapytanie
    return render(request, 'coapp/desk_list.html', {'desks': desks})


@login_required
def reserve_desk(request, desk_id):
    desk = get_object_or_404(Desk, id=desk_id)
    error_messages = []
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            today = timezone.localdate()

            if start_date < today:
                error_messages.append('Data rezerwacji nie może być wcześniejsza od dzisiejszej.')
            elif end_date <= start_date:
                error_messages.append('Data zakończenia musi być późniejsza niż data rozpoczęcia.')

            if not error_messages:
                total_days = (end_date - start_date).days + 1
                total_cost = desk.price * total_days
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.desk = desk
                reservation.total_cost = total_cost
                reservation.save()
                desk.status = 'zajęte'
                desk.save()
                return redirect('reservation_confirmation', reservation_id=reservation.id)
        else:
            error_messages.append('Formularz zawiera błędy.')

    else:
        form = ReservationForm(initial={'desk': desk})

    return render(request, 'coapp/reservation_form.html',
                  {'form': form, 'desk': desk, 'error_messages': error_messages})


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


def cancel_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id, user=request.user)
        desk = reservation.desk
        desk.status = 'czynne'
        desk.save()
        reservation.delete()
        messages.success(request, 'Rezerwacja została anulowana.')
    except Reservation.DoesNotExist:
        messages.error(request, 'Nie znaleziono rezerwacji.')
    return redirect('user_reservations')


def home(request):
    """Wyświetla stronę główną."""
    return render(request, "coapp/home.html", {})


def offer(request):
    """Wyświetla ofertę biurek."""
    return render(request, 'coapp/offer.html')


def contact(request):
    """Wyświetla stronę kontaktową."""
    return render(request, 'coapp/contact.html')


class MyLoginView(LoginView):
    """Widok logowania z przekierowaniem zalogowanych użytkowników."""
    template_name = 'coapp/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
