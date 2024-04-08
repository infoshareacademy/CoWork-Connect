from django.shortcuts import render

# Create your views here.
def home(response):
    response.user
    return render(response, "coapp/home.html", {})
