from django import forms
from .models import Pins

class CreatePin(forms.ModelForm):
    class Meta:
        model = Pins
        fields = ['name', 'slug', 'pin', 'notes', 'user_id']
        widgets = {'slug': forms.HiddenInput(), 'user_id': forms.HiddenInput()}