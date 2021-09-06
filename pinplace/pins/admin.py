from django.contrib import admin
from .models import Pins

# Register your models here.

class PinAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Pins, PinAdmin)