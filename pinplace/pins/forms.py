from django import forms
from .models import Pins

class CreatePin(forms.ModelForm):
    class Meta:
        model = Pins
        fields = ['name', 'slug', 'pin', 'notes']