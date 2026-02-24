from django.contrib import admin
from .models import DeliveryRider


@admin.register(DeliveryRider)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number', 'vehicle_name', 'vehicle_number', 'created_at', 'updated_at')
    list_filter = ('created_at', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
    