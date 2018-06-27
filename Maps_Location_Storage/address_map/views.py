from django.shortcuts import render
from .models import Location
from .forms import CreateForm


def maps(request):
    return render(request, 'address_map/G_maps.html')


def index(request):
    all_companies = Location.objects.all()
    return render(request, 'address_map/index.html', {'companies': all_companies})


def create(request):
    if request.method == 'POST':
        pass

    else:
        form = CreateForm()
        return render(request, 'address_map/create_form.html', {'form': form})


