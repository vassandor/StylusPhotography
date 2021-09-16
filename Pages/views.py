from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("<h1>Stylus Photography: Home</h1>")

def contact_page(request):
    return HttpResponse("<h1>Stylus Photography: Contact</h1>")

def about_page(request):
    return HttpResponse("<h1>Stylus Photography: About</h1>")

def gallery_page(request):
    return HttpResponse("<h1>Stylus Photography: Gallery</h1>")