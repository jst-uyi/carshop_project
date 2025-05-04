from django.contrib import admin
from .models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'fuel_type', 'transmission', 'owner_type', 'year', 'kilometers',)
    list_filter = ('fuel_type', 'name', 'transmission', 'owner_type', 'year', 'kilometers',)
    search_fields = ('name', 'location')
    ordering = ('-price',)

