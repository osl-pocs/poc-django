from django.contrib.auth import models as auth_models
from django.db import models

from djangopoc.users.managers import UserManager


class User(auth_models.AbstractUser):
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        verbose_name='organization',
        null=False,
    )

    objects = UserManager()


class Organization(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
