from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class Account(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    username = None
    phone = models.CharField(max_length=11)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
