from django.contrib import admin
from .models import Desk, Settings

@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('stock_number', 'size', 'monitor_number', 'power_socket_count', 'price', 'status')
    list_filter = ('monitor_number', 'size', 'status')
    search_fields = ['stock_number']


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
