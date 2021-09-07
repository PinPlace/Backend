from users.models import Users
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

class Pins(models.Model):
    pin_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100)
    tags = TaggableManager()
    pin = models.TextField()
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    class Meta:
        verbose_name_plural = "Pins"

    def __str__(self):
        return f"{self.name} | {self.tags}"  

    def snippet(self):
        return self.pin[:50] + '...'