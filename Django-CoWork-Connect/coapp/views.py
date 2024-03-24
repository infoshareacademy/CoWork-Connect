from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "coapp/home.html", {})

def offer(response):
    return render(response, "coapp/offer.html", {})

def avaliability(response):
    return render(response, "coapp/avaliability.html", {})

def pricelist(response):
    return render(response, "coapp/pricelist.html", {})
def reservation(response):
    return render(response, "coapp/reservation.html", {})
def regulations(response):
    return render(response, "coapp/regulations.html", {})
def contact(response):
    return render(response, "coapp/contact.html", {})