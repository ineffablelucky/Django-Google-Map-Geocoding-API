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
                   'id': 'locality',
                   'placeholder': 'city'}))

    state = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control states',
                   'id': 'administrative_area_level_1',
                   'placeholder': 'state'}))

    country = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'text',
                   'class': 'form-control country',
                   'id': 'country',
                   'placeholder': 'country'}))

    lat = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'hidden',
                   'class': 'form-control lat',
                   'id': 'add_lat'}))

    lng = forms.CharField(max_length=100, required=False, strip=True, widget=forms.TextInput(
            attrs={'type': 'hidden',
                   'class': 'form-control lng',
                   'id': 'add_lng'}))

    class Meta:

        model = Location
        fields = '__all__'
