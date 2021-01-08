from django.contrib import admin

# Register your models here.
from myapp.models import Customer, User, Product, Brand


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

