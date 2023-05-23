from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    objects = CustomUserManager()
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='',unique=True)
    USERNAME_FIELD = 'name'
    username=None
    # REQUIRED_FIELDS=['name']

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['created']
