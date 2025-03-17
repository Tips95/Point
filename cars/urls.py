from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('conditions/', views.conditions, name='conditions'),
    path('add-car/', views.add_car, name='add_car'),
    path('delete-car/<int:car_id>/', views.delete_car, name='delete_car'),
]