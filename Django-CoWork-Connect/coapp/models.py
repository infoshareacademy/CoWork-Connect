from django.db import models
from django.contrib.auth.models import User

class Desk(models.Model):
    stock_number = models.CharField(max_length=50)
    size = models.IntegerField()
    monitor_number = models.IntegerField(default=0)
    power_socket_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Biurko nr {self.stock_number}, Ilość stanowisk/biurko: {self.size}, Ilość monitorów/stanowisko: {self.monitor_number}, Ilość gniazdek/biurko: {self.power_socket_count}, Cena: {self.price} zł, Status: {self.status}"

class Reservation(models.Model):
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rezerwacja {self.id} - Użytkownik: {self.user.username}"