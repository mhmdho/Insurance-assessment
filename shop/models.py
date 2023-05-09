from django.db import models
from user.models import CustomUser

# Create your models here.

class Shop(models.Model):
    """
    Shops of website, each user can create more than one shop.
    """
    ELE = "ELECTRONICS"
    CLO = "CLOTHING"
    JEW = "JEWELRY"

    TYPE_CHOICES = (
        (ELE, "Electronics"),
        (CLO, "Clothing"),
        (JEW, "Jewelry"),
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=17, choices=TYPE_CHOICES, default=ELE)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
  