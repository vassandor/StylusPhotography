from django.shortcuts import render, HttpResponse
from utilities.data_gen import create_photo_list

# Create your views here.

def home_page(request):
    return render(request, "home.html")

def contact_page(request):
    return render(request, "contact.html")

def about_page(request):
    return render(request, "about.html")

def gallery_page(request):
    return render(request, "gallery.html", {"images": create_photo_list(10)})
