from django import forms
from .models import Location


class CreateForm(forms.ModelForm):

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
