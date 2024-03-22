from .forms import RegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
#
# # Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('home')