from django.contrib import admin

# Register your models here.
from myapp.models import Customer, User, Product, Brand, Product_Detail, Product_List


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'brand')


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('specific', 'color')


#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass

#
# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     pass

admin.site.register(User )
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Product_Detail, ProductDetailAdmin)
admin.site.register(Product_List)
