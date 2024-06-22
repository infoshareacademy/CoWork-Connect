from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Reservation

@shared_task
def send_confirmation_email(reservation_id, user_email):
    reservation = Reservation.objects.get(id=reservation_id)
    subject = 'Potwierdzenie rezerwacji'
    html_message = render_to_string('coapp/confirmation_email.html', {'reservation': reservation})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user_email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

@shared_task
def send_cancellation_email(reservation_id, user_email, desk_stock_number, start_date, end_date, total_cost):
    subject = 'Anulowanie rezerwacji'
    context = {
        'reservation_id': reservation_id,
        'desk_stock_number': desk_stock_number,
        'start_date': start_date,
        'end_date': end_date,
        'total_cost': total_cost
    }
    html_message = render_to_string('coapp/cancellation_email.html', context)
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user_email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)