# second/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
