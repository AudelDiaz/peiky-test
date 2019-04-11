from django.db import models

from stores.models import Store


class Product(models.Model):
    class Meta:
        ordering = ['id']

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products/images/', null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    class Meta:
        ordering = ['id']
        unique_together = 'product', 'name'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=100)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.name
