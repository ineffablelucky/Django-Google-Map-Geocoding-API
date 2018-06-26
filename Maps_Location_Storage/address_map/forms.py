from django import forms
from .models import Location


class CreateForm(forms.ModelForm):
    # name = models.CharField(max_length=100)
    # lat = models.DecimalField('Latitude', max_digits=10, decimal_places=8)
    # lng = models.DecimalField('Longitude', max_digits=10, decimal_places=8)
    # address = models.CharField(max_length=500, null=True, blank=True)
    # city = models.CharField(max_length=100, null=True, blank=True)
    # state = models.CharField(max_length=100, null=True, blank=True)
    # country = models.CharField(max_length=100, null=True, blank=True)

    name = forms.CharField(max_length=100)

    address = forms.CharField(max_length=500)

    city = forms.CharField(max_length=100)

    state = forms.CharField(max_length=100)

    country = forms.CharField(max_length=100)

    class Meta:

        model = Location
        exclude = ('lat', 'lng')
