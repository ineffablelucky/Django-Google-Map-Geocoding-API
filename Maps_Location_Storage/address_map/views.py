from django.shortcuts import render, redirect, get_object_or_404
from .models import Location
from .forms import CreateForm


def index(request):
    all_places = Location.objects.all()  # getting all objects from Location model
    return render(request, 'address_map/index.html', {'places': all_places})


def create(request):
    if request.method == 'POST':

        form = CreateForm(request.POST)  # created form object with data received at POST request

        if form.is_valid():
            form.save()   # calling save() method in forms.py
            return redirect('index')

    else:

        form = CreateForm()  # getting form during a GET request

    return render(request, 'address_map/create_form.html', {'form': form})


def update(request, pk):
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=Location.objects.get(id=pk))

        if form.is_valid():
            form.save()

            return redirect('index')

    else:
        form = CreateForm(instance=get_object_or_404(Location, id=pk))

    return render(request, 'address_map/update_form.html', {'form': form})
