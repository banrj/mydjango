from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        db_table = 'Profile'


class Product(models.Model):
    product_name = models.CharField(max_length=25, verbose_name='Название')
    price = models.IntegerField()
    options = models.TextField(max_length=100, verbose_name='Описание', null=True)
    created_by = models.ForeignKey(Profile, related_name='creater', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Products'
        ordering = ['created_by', 'id']


class Order(models.Model):
    address = models.TextField(null=True, blank=True)
    promo_code = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(Profile, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product)
