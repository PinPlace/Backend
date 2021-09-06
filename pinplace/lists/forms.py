from django import forms
from django.forms import widgets
from .models import Lists

class CreateList(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['name', 'slug', 'colour', 'thumb' ]
        widgets = {'slug': forms.HiddenInput()}