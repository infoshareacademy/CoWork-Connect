from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Reservation, Desk, Settings
from .forms import ReservationForm
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'coapp/reservation_form.html'
    success_url = reverse_lazy('home')  # Przekierowanie po pomyślnej rezerwacji


def home(request):
    return render(request, "coapp/home.html", {})
def offer(request):
    # Logika dla widoku
    return render(request, 'coapp/offer.html')


def cancel_reservation(request):
    return render(request, 'coapp/cancel_reservation.html')

def pricing(request, id):
    return render(request, 'coapp/pricing.html')

def contact(request):
    contact_fields = Settings.objects.all()
    return render(request, 'coapp/contact.html', {'contact_fields': contact_fields})


class MyLoginView(LoginView):
    template_name = 'coapp/login.html'
    redirect_authenticated_user = True  # Przekierowuje zalogowanych użytkowników do strony głównej

    def get_success_url(self):
        return reverse_lazy('home')  # Nazwa URL strony, do której użytkownik zostanie przekierowany po pomyślnym logowaniu

def desk_list(request):
    desks = Desk.objects.all()
    return render(request, 'coapp/desk_list.html', {'desks': desks})
def reservation(request):
    desks = Desk.objects.all()  # Pobierasz wszystkie biurka z bazy danych
    return render(request, 'coapp/reservation_form.html', {'desks': desks})

# Create your views here.
def home(response):
    response.user
    return render(response, "coapp/home.html", {})

