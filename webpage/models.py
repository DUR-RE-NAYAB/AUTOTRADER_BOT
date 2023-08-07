from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200000000,null=False)
    product_price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)


    