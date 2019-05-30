from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Category"

class Vendor(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.ForeignKey('auth.User',on_delete="delete")
    name = models.CharField(max_length=200)
    address =  models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    status = models.IntegerField(max_length=1)

    class Meta:
        verbose_name_plural = "Vendor"

class Product(models.Model):
    id = models.IntegerField(primary_key=True)   
    name = models.CharField(max_length=200) 
    category_id = models.ForeignKey(Category,on_delete="delete")    
    product_type =  models.CharField(max_length=100)
    skucode = models.CharField(max_length=100)
    status = models.IntegerField(max_length=1)
    description = models.TextField(null=True)
    short_description = models.CharField(max_length=500)
    status = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = "Product"