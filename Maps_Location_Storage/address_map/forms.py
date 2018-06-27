from django import forms
from .models import Location


class CreateForm(forms.ModelForm):
    # name = models.CharField(max_length=100, blank=true)
    # lat = models.DecimalField('Latitude', max_digits=10, decimal_places=8)
    # lng = models.DecimalField('Longitude', max_digits=10, decimal_places=8)
    # address = models.CharField(max_length=500, null=True, blank=True)
    # city = models.CharField(max_length=100, null=True, blank=True)
    # state = models.CharField(max_length=100, null=True, blank=True)
    # country = models.CharField(max_length=100, null=True, blank=True)

    name = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control names',
                   'id': 'add_name',
                   'placeholder': 'name'}))

    address = forms.CharField(max_length=500, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control address',
                   'id': 'add_address',
                   'placeholder': 'address',
                   'readonly': True}))

    city = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control city',
                   'id': 'add_city',
                   'placeholder': 'city'}))

    state = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control states',
                   'id': 'add_state',
                   'placeholder': 'state'}))

    country = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control country',
                   'id': 'add_country',
                   'placeholder': 'country'}))

    class Meta:

        model = Location
        exclude = ('lat', 'lng')
