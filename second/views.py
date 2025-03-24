# second/views.py
from django.http import HttpResponse

def services(request):
    return HttpResponse("<h1>Our Services</h1><p>We provide top-notch services!</p>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>Email us at contact@example.com</p>")
