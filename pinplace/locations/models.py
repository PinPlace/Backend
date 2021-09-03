from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Locations(models.Model):
    name = models.CharField(max_length=200, blank=False)
    tags = TaggableManager(blank=False)
    locations = models.TextField(blank=False)
    notes = models.TextField()

    # def __str__(self):
    #     return self.name