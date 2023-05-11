from django.db import models
from user.models import CustomUser
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify
import random

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


class Product(models.Model):
    """
    products of each shop. Each product belongs only to one shop.
    """
    slug = models.SlugField(max_length=70, blank=True, unique=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    stock = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=400)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, related_name='shop_products')

    class Meta:
        ordering = ['-id']

    def random_number_generator(self):
        return '_' + str(random.randint(1000, 9999))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            while Product.objects.filter(slug = self.slug):
                self.slug = slugify(self.name)
                self.slug += self.random_number_generator()
        if self.stock == 0:
            self.is_active = False
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
