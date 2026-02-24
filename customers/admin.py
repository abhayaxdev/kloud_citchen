from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'created_at', 'updated_at')
    list_filter = ('created_at', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
    