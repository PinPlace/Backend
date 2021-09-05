from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=75, blank=False)
    # password = PasswordInput()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username