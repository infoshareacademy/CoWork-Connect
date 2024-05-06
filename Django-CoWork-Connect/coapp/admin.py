from django.contrib import admin
from .models import Desk, Reservation

class DeskAdmin(admin.ModelAdmin):
    list_display = ('name', 'monitors', 'size', 'sockets', 'price', 'status')
    list_filter = ('status', 'size')
    search_fields = ('name', 'status')
    actions = ['cancel_reservations']
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('desk', 'id', 'user', 'start_date', 'end_date', 'total_cost')
    list_filter = ('start_date', 'end_date', 'user')
    search_fields = ('id', 'user__username', 'desk__name')
    raw_id_fields = ('desk', 'user')

    def cancel_reservations(self, request, queryset):
        for reservation in queryset:
            desk = reservation.desk
            desk.status = 'czynne'
            desk.save()
            reservation.delete()
        self.message_user(request, "Wybrane rezerwacje zostały anulowane i statusy biurek zaktualizowane.")

    cancel_reservations.short_description = "Anuluj wybrane rezerwacje i aktualizuj status biurek"


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Desk, DeskAdmin)

