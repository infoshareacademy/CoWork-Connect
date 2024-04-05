from django.shortcuts import render
from .models import Desk

# Create your views here.
def home(response):
    return render(response, "coapp/home.html", {})
def desk_list(request):
    desks = Desk.objects.all()  # Pobieranie wszystkich biurek z bazy danych
    return render(request, 'coapp/desk_list.html', {'desks': desks})