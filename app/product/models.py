from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    class_type = models.CharField(
        max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_creator")
    image = models.ImageField(upload_to='image/', default='image/default.jpg')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created_on',)

    def __str__(self):
        return self.title
