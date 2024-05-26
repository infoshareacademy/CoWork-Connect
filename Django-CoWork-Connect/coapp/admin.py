from django.contrib import admin
from .models import Desk, Reservation, OurOffer, ContactForm


class DeskAdmin(admin.ModelAdmin):
    list_display = ('stock_number', 'size', 'monitor_number', 'power_socket_count', 'price', 'status')
    list_filter = ('monitor_number', 'size', 'status')
    search_fields = ['stock_number', 'status']
    actions = ['cancel_reservations']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('desk', 'id', 'user', 'start_date', 'end_date', 'total_cost')
    list_filter = ('start_date', 'end_date', 'user')
    search_fields = ('id', 'user__username', 'desk__name')
    raw_id_fields = ('desk', 'user')

    def cancel_reservations(self, request, queryset):
        desk_ids = queryset.values_list('desk__id', flat=True)
        Desk.objects.filter(id__in=desk_ids).update(status='czynne')
        queryset.delete()
        self.message_user(request, "Wybrane rezerwacje zostały anulowane i statusy biurek zaktualizowane.")

    cancel_reservations.short_description = "Anuluj wybrane rezerwacje i aktualizuj status biurek"

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Desk, DeskAdmin)

@admin.register(OurOffer)
class OurOfferAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass
