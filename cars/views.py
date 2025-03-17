from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car
from .forms import CarForm, CarImageForm
from django.contrib import messages

def home(request):
    cars = Car.objects.all()[:3]
    return render(request, 'cars/home.html', {'cars': cars})

def catalog(request):
    cars = Car.objects.all()
    return render(request, 'cars/catalog.html', {'cars': cars})

def conditions(request):
    return render(request, 'cars/conditions.html')

@login_required
def add_car(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST)
        image_form = CarImageForm(request.POST, request.FILES)
        
        if car_form.is_valid() and image_form.is_valid():
            car = car_form.save()
            image = image_form.save(commit=False)
            image.car = car
            image.save()
            messages.success(request, 'Машина успешно добавлена!')
            return redirect('catalog')
    else:
        car_form = CarForm()
        image_form = CarImageForm()
    
    return render(request, 'cars/add_car.html', {
        'car_form': car_form,
        'image_form': image_form
    })

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Машина успешно удалена!')
        return redirect('catalog')
    return render(request, 'cars/delete_car.html', {'car': car})