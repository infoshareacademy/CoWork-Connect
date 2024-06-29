from django.urls import path
from .views import RegisterView  # Upewnij się, że masz taki widok w views.py

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]
