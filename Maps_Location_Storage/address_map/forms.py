from django import forms
from .models import Location
from django.contrib.gis.geos import Point


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
                   'readonly': True}))  # read-only as we want it to be auto-filled when clicked on map

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

    '''
    created form fields named as 'lat' and 'lng' to save the coordinates individually
    '''
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
        exclude = ('coordinate',)  # saved in def save() function using lat and lng values from form

    def save(self, commit=True):

        entry = super().save(commit=False)
        latitude = float(self.cleaned_data.get('lat'))  # using float instead of int as coordinates are large digit nums
        longitude = float(self.cleaned_data.get('lng'))

        entry.coordinate = Point(latitude, longitude)  # 'Point' imported above

        if commit:
            entry.save()

        return entry
