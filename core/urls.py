from django.contrib import admin
from django.urls import path
from pages.views import home, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('admin/', admin.site.urls),
]
