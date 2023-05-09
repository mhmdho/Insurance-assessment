from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class CustomUser(AbstractUser):
  """
  Customize django user and add phone to it.
  """
  phone_regex = RegexValidator(regex=r'^09\d{9}$',
                               message="Phone number must be entered in the format: '+989121234567'.")
  
  phone = models.CharField(validators=[phone_regex], max_length=11, unique=True)
  last_login = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.phone
