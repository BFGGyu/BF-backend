from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from place.models import Facility

class Member(AbstractUser):
    age = models.IntegerField(verbose_name="나이",default=20, null=True)
