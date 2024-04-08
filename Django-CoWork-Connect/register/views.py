from .forms import RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
#
# # Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('home')

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    pass