from django.contrib import admin

# Register your models here.
from myapp.models import Customer, User, Product, Brand


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')


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

admin.site.register(User, CustomerAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Brand)
