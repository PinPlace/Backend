from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Pins(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField()
    tags = TaggableManager()
    pin = models.TextField()
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    # author = 
    #slug is url address of the pin

    class Meta:
        verbose_name_plural = "Pins"

    def __str__(self):
        return f"{self.name} | {self.tags}"  

    def snippet(self):
        return self.pin[:50] + '...'

