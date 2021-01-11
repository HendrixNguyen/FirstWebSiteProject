"""CNPM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.redirects.models import Redirect
from django.shortcuts import redirect
from django.urls import path

from django.conf import settings
from django.views.generic import RedirectView

from myapp.views import HomeView, GalleryView, AboutView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', RedirectView.as_view(url='home/')),
    path('home/', HomeView.as_view()),
    path('gallery/', GalleryView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# def home():
#     if urlpatterns == "/":
#         return redirect(HomeView.as_view)