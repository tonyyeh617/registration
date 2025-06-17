from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    cBirthday = models.DateField(null=True, blank=True, verbose_name="生日")
    tel = models.CharField(max_length=16, null=True, blank=True, verbose_name="電話")


    def __str__(self):
        return self.username
