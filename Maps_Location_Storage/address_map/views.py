from django.shortcuts import render, redirect
from .models import Location
from .forms import CreateForm


def maps(request):
    return render(request, 'address_map/G_maps.html')


def index(request):
    all_companies = Location.objects.all()  # getting all objects from Location model
    return render(request, 'address_map/index.html', {'companies': all_companies})


def create(request):
    if request.method == 'POST':

        form = CreateForm(request.POST)  # created form object with data received at POST request

        if form.is_valid():
            form.save()   # calling save() method in forms.py
            return redirect('index')

    else:

        form = CreateForm()  # getting form during a GET request

    return render(request, 'address_map/create_form.html', {'form': form})


