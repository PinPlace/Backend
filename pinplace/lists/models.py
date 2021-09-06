from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lists(models.Model):
    name = models.CharField(max_length=100, blank=False)
    thumb = models.ImageField(default='default.png', blank=True)
    colour = ColorField(default='#FF0000')
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Lists"

    def __str__(self):
        return self.name

'''
if we want to specify color choices, add the below to the above
class MyModel(model.Model):

    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black")
    ]

    color = ColorField(choices=COLOR_CHOICES)
'''

