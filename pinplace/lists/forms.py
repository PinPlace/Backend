from django import forms
from django.forms import widgets
from .models import Lists

class CreateList(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['name', 'slug', 'colour', 'thumb', 'user_id', 'pins_id']
        widgets = {
            'slug': forms.HiddenInput(),
            'user_id': forms.HiddenInput(),
            # 'pins_id': forms.HiddenInput(),
            }