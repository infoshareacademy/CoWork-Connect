from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("offer/", views.offer, name="offer"),
    path("avaliability/", views.avaliability, name="avaliability"),
    path("pricelist/", views.pricelist, name="pricelist"),
    path("reservation/", views.reservation, name="reservation"),
    path("regulations/", views.regulations, name="regulations"),
    path("contact/", views.contact, name="contact")
]

