from django import forms
from .models import Car, CarImage

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'name', 'year', 'transmission', 'engine_volume', 'fuel_consumption',
            'drive_type', 'rental_schedule', 'redemption_period', 'osago',
            'price_per_day', 'mileage'
        ]
        widgets = {
            'transmission': forms.Select(),
            'drive_type': forms.Select(),
        }

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image', 'is_main']