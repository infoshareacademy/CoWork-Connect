from django.db import models
from django.contrib.auth.models import User

class Desk(models.Model):
    stock_number = models.CharField(max_length=50)  # numer biurka
    size = models.IntegerField()  # ilość stanowisk na biurko
    monitor_number = models.IntegerField()  # ilość monitorów na stanowisko
    power_socket_count = models.IntegerField(default=1)  # ilość gniazdek na biurko
    price = models.DecimalField(max_digits=6, decimal_places=2)  # cena
    status = models.CharField(max_length=50)  # status, np. "czynne"

    def update_status(self, new_status):
        self.status = new_status
        self.save()
    def __str__(self):
        return (f"Biurko nr {self.stock_number}")

class Reservation(models.Model):
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rezerwacja {self.id} - Użytkownik: {self.user.username}"