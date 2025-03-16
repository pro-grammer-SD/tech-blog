from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.TextField(default="Enter title here...")
    description = models.TextField(default="Enter description here...")
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', height_field=None, width_field=None, max_length=100, default='products/default.jpg')