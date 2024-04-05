from django.db import models
class Desk(models.Model):
    desk_type = models.CharField(max_length=255)
    monitor = models.BooleanField(default=False)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"Biurko {self.id} - Rozmiar: {self.size}, {'z monitorem' if self.monitor else 'bez monitora'}"