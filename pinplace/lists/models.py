from colorfield.fields import ColorField
from django.db import models
from django.contrib.auth.models import User
# from users.models import Users
from pins.models import Pins

# Create your models here.

class Lists(models.Model):
    name = models.CharField(max_length=100, blank=False)
    thumb = models.CharField(max_length=100, blank=True)
    colour = ColorField(default='#FF0000')
    slug = models.SlugField(max_length=100)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # pin_id = models.ForeignKey(Pins, on_delete=models.CASCADE, blank=True)

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

 # pins_id = models.ForeignKey(Pins, on_delete=models.CASCADE, blank=True)

