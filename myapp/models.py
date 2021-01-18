from django.db import models


# Create your models here.
class User(models.Model):
    JOB_MANAGER = "Quản Lý"
    JOB_STAFF = "Tư Vấn"
    # Enumrable
    JOBS = [
        ("manager", JOB_MANAGER),
        ("staff", JOB_STAFF),
    ]

    name = models.CharField(max_length=255, null=None)
    phone_number = models.CharField(max_length=190, null=None)
    email = models.EmailField(max_length=100, blank=True, null=None)
    address = models.CharField(max_length=255, unique=True, null=None)
    Faculty = models.CharField(max_length=20, choices=JOBS, default=JOB_STAFF, null=None)
    #
    # def __str__(self):
    #     return self.email


class Customer(models.Model):
    name = models.CharField(max_length=255, null=None)
    phone_number = models.CharField(max_length=190)
    email = models.EmailField(max_length=255, blank=True)
    address = models.CharField(max_length=255, unique=True, null=True)
    respones = models.TextField(null=True)
    staff = models.ForeignKey('myapp.User', on_delete=models.CASCADE)


class Product(models.Model):
    product_name = models.CharField(max_length=255, null=None)
    picture = models.FileField(upload_to='uploads')
    video = models.FileField(null=True, blank=True)
    brand = models.ForeignKey('myapp.Brand', on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     return self.product_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, null=None)


class Product_Detail(models.Model):
    specific = models.TextField()
    color = models.CharField(max_length=20, null=True, blank=True)
    product = models.ForeignKey('myapp.Product', on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     return self.product


class Product_List(models.Model):
    name = models.CharField(max_length=190)
    prolist = models.ManyToManyField('myapp.Product')
