from django.contrib import admin
from .models import Desk

@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    list_display = ('name', 'desk_type', 'monitor', 'size', 'price', 'status')
    list_filter = ('monitor', 'size', 'status')
    search_fields = ('name', 'desk_type')
