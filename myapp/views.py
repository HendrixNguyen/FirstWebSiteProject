from django.shortcuts import render
from django.views import View

from myapp.models import Customer, Product


class HomeView(View):
    # Func get to take the data from model
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.filter(respones__isnull=False).all()
        # render a templates with a variable
        return render(request, 'index.html', {
            'customers': customers,
        })


class GalleryView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, 'gallery.html', {
            'products': products,
            'loop': range(50),
        })


class AboutView(View):
    def get(self, request, *args, **kwargs):
        # customers = Customer.objects.filter(respones__isnull=False).all()
        #
        # return render(request, 'index.html', {
        #     'customers': customers,
        # })
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request, *args, **kwargs):
        # customers = Customer.objects.filter(respones__isnull=False).all()
        #
        # return render(request, 'index.html', {
        #     'customers': customers,
        # })
        return render(request, 'contact.html')
