from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import ReservationCreateView, desk_list
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='coapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', include('register.urls')),path('offer/', views.offer, name='offer'),
    path('desks/', desk_list, name='desk_list'),
    path('reservation/', ReservationCreateView.as_view(), name='reservation_form'),
    path('cancel_reservation/', views.cancel_reservation, name='cancel_reservation'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
]