from django.contrib import admin
from .models import Category, Photo
# Register your models here.

admin.site.register(Category)

class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "homepage", "image"]
    list_editable = ["homepage"]
    list_filter = ["category"]
    search_fields = ["title"]

admin.site.register(Photo, PhotoModelAdmin)