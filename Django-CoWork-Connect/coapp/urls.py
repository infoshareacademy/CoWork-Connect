from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import desk_list
from . import views
from .views import user_reservations
from .views import cancel_reservation

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='coapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', include('register.urls')),
    path('offer/', views.offer, name='offer'),
    path('desks/', desk_list, name='desk_list'),
    path('contact/', views.contact, name='contact'),
    path('reserve/<int:desk_id>/', views.reserve_desk, name='reserve_desk'),
    path('reservation/<int:reservation_id>/', views.reservation_confirmation, name='reservation_confirmation'),
    path('reservations/', user_reservations, name='user_reservations'),
    path('cancel-reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('terms/', views.term, name='terms'),

]
