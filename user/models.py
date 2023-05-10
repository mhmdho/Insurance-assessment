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

  groups = models.ManyToManyField(
      "auth.Group",
      blank=True,
      related_name="custom_user_groups",
      help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
      verbose_name="groups",
  )
  user_permissions = models.ManyToManyField(
      "auth.Permission",
      blank=True,
      related_name="custom_user_permissions",
      help_text="Specific permissions for this user.",
      verbose_name="user permissions",
  )
  
  USERNAME_FIELD = 'phone'

  def __str__(self):
      return self.phone
