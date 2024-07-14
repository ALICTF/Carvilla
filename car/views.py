from django.shortcuts import render
from django.views.generic import ListView

from .models import Brand, Car

def home_view(request):
    context = {}
    return render(request, 'car/index.html', context)
