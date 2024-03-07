from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    SIZE = (
        ('25sm', '25sm'),
        ('35sm', '35sm'),
        ('45sm', '45sm'),
    )
    name = models.CharField(max_length=150)
    size = models.CharField(max_length=50, choices=SIZE)
    image = models.ImageField(upload_to='pizza/')
    price = models.FloatField(default=0)
    ingredient = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Cancelled', 'Cancelled'),
        ('Cooking', 'Cooking'),
        ('Delivering', 'Delivering'),
        ('Done', 'Done'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username