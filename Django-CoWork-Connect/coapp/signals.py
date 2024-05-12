from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reservation, Desk


@receiver(post_save, sender=Reservation)
def update_desk_status(sender, instance, created, **kwargs):
    desk = instance.desk
    if created:
        desk.status = 'zajęte'
    else:
        # Można tutaj dodać logikę do obsługi aktualizacji rezerwacji.
        # Na przykład, sprawdzenie czy rezerwacja została anulowana i aktualizacja statusu biurka.
        pass
    desk.save()
