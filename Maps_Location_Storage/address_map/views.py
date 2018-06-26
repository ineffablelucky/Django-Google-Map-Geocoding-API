from django.shortcuts import render
from .models import Location


def maps(request):
    return render(request, 'address_map/G_maps.html')


def index(request):
    all_companies = Location.objects.all()
    return render(request, 'address_map/index.html', {'companies': all_companies})