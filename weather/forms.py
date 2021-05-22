from django import forms


class LocationCoordinateForm(forms.Form):
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()
