from django.db import models
from django.contrib.auth.models import User

class Desk(models.Model):
    stock_number = models.CharField(max_length=50)  # numer biurka
    size = models.IntegerField()  # ilość stanowisk na biurko
    monitor_number = models.IntegerField(null=True)  # ilość monitorów na stanowisko
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


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1  # Ensure the primary key is always 1
        if self.__class__.objects.exists() and not self.pk:
            self.pk = self.__class__.objects.first().pk
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Prevent deletion of singleton instance

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class OurOffer(SingletonModel):
    title = models.CharField(max_length=50)
    description_1_subtitle = models.TextField(default="Insert your title for first paragraph...")
    description_1 = models.TextField(default="Insert your first paragraph's description...")
    description_2_subtitle = models.TextField(default="", blank=True)
    description_2 = models.TextField(default="", blank=True)

class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)