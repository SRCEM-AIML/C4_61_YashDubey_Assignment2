# first/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse('''
    <h1>Welcome to Home Page</h1>
    <p><a href="/about/">About Us</a></p>
    <p><a href="/second/services/">Our Services</a></p>
    <p><a href="/second/contact/">Contact Us</a></p>
    ''')

def about(request):
    return HttpResponse("<h1>About Us</h1><p>We are a leading company!</p>")
