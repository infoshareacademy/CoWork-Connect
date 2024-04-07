from django.db import models

class Desk(models.Model):
    stock_number = models.CharField(max_length=50)
    size = models.IntegerField()
    monitor_number = models.IntegerField(default=0)
    power_socket_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Biurko nr {self.stock_number}, Ilość stanowisk/biurko: {self.size}, Ilość monitorów/stanowisko: {self.monitor_number}, Ilość gniazdek/biurko: {self.power_socket_count}, Cena: {self.price} zł, Status: {self.status}"
