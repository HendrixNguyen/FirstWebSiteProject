from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=None)
    phone_number = models.CharField(max_length=190)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=255, unique=True)
    Faculty = models.CharField(max_length=15)

    def __str__(self):
        self.name


class Customer(models.Model):
    name = models.CharField(max_length=255, null=None)
    phone_number = models.CharField(max_length=190)
    email = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, unique=True, null=True)
    respones = models.TextField(null=True)
    staff = models.ForeignKey('myapp.User', on_delete=models.CASCADE)


class Product(models.Model):
    product_name = models.CharField(max_length=255, null=None)
    picture = models.FileField(upload_to='uploads')
    video = models.FileField(null=True, blank=True)
    brand = models.ForeignKey('myapp.Brand', on_delete=models.CASCADE)


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, null=None)


class Product_Detail(models.Model):
    specific = models.TextField()
    color = models.CharField(max_length=20, null=True, blank=True)
    product = models.ForeignKey('myapp.Product', on_delete=models.CASCADE)


class Product_List(models.Model):
    name = models.CharField(max_length=190)
    prolist = models.ManyToManyField('myapp.Product')
