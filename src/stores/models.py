from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/')
    slug = models.SlugField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
