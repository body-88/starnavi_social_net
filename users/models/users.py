from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    last_activity = models.DateTimeField(default=None, null=True)
