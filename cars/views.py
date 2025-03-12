from django.shortcuts import render
from .models import Car


def home(request):
    cars = Car.objects.all()[:3]
    return render(request, 'cars/home.html', {'cars': cars})

def catalog(request):
    cars = Car.objects.all()
    return render(request, 'cars/catalog.html', {'cars': cars})

def conditions(request):
    return render(request, 'cars/conditions.html')