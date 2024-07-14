from django.shortcuts import render
from django.views.generic import ListView

from .models import Brand, Car

def home_view(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    
    context = {
        'cars': cars,
        'brands': brands
    }

    return render(request, 'car/home.html', context)
