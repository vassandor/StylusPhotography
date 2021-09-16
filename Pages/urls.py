from django.urls import path
from .views import home_page, gallery_page, about_page, contact_page

urlpatterns = [
    path('', home_page),
    path('gallery/', gallery_page),
    path('about/', about_page),
    path('contatct/', contact_page),
]