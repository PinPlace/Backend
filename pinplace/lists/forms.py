from pins.models import Pins
from django import forms
from django.forms import widgets
from .models import Lists

class CreateList(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['name', 'slug', 'colour', 'thumb', 'user_id']
        widgets = {
            'slug': forms.HiddenInput(),
            'user_id': forms.HiddenInput(),
            }

class CreateListPin(forms.ModelForm):
    class Meta:
        model: Pins
        fields = ['pin_id', 'name']
        widgets = {
            'slug': forms.HiddenInput(),
            'user_id': forms.HiddenInput(),
        }


# pin_id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=100, blank=False)
#     slug = models.SlugField(max_length=100)
#     tags = TaggableManager()
#     pin = models.TextField()
#     notes = models.TextField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     # author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
#     user_id =