from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("<h1>Stylus Photography Home</h1>")