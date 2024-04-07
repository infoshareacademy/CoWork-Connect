from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("desks/", views.desk_list, name="desk_list"),
]