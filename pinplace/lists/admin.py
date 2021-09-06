from django.contrib import admin
from .models import Lists

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Lists, ListAdmin)