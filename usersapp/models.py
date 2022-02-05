from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(unique=True, max_length=64, blank=False)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True, blank=False)
