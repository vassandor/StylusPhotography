from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page(request):
    return render(request, "home.html")

def contact_page(request):
    return render(request, "contact.html")

def about_page(request):
    return render(request, "about.html")

def gallery_page(request):
    return render(request, "gallery.html")