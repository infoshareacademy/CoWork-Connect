from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Reservation, Desk
from .forms import ReservationForm
from django.views.generic import View

class ReservationView(View):
    form_class = ReservationForm
    template_name = 'coapp/reservation_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Zmodyfikuj na właściwy URL
        return render(request, self.template_name, {'form': form})
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'coapp/reservation_form.html'
    success_url = reverse_lazy('home')  # Przekierowanie po pomyślnej rezerwacji
# def home(response):
#     return render(response, "coapp/home.html", {})
def home(request):
    return render(request, "coapp/home.html", {})
def offer(request):
    # Logika dla widoku
    return render(request, 'coapp/offer.html')
def reservation(request):
    return render(request, 'coapp/reservation_form.html')

def cancel_reservation(request):
    return render(request, 'coapp/cancel_reservation.html')

def pricing(request, id):
    return render(request, 'coapp/pricing.html')

def contact(request):
    return render(request, 'coapp/contact.html')


class MyLoginView(LoginView):
    template_name = 'coapp/login.html'
    redirect_authenticated_user = True  # Przekierowuje zalogowanych użytkowników do strony głównej

    def get_success_url(self):
        return reverse_lazy('home')  # Nazwa URL strony, do której użytkownik zostanie przekierowany po pomyślnym logowaniu

def desk_list(request):
    desks = Desk.objects.all()
    return render(request, 'coapp/desk_list.html', {'desks': desks})
