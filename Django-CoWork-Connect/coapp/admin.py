from django.contrib import admin
from .models import Desk, OurOffer

@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('stock_number', 'size', 'monitor_number', 'power_socket_count', 'price', 'status')
    list_filter = ('monitor_number', 'size', 'status')
    search_fields = ['stock_number']


@admin.register(OurOffer)
class OurOfferAdmin(admin.ModelAdmin):
    pass