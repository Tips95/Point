from django.contrib import admin
from .models import Car, CarImage

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'price_per_day', 'mileage')
    list_filter = ('year', 'transmission', 'drive_type')
    search_fields = ('name',)
    inlines = [CarImageInline]

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'is_main')
    list_filter = ('car', 'is_main')