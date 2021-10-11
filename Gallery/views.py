# Create your views here.
from django.views.generic import DetailView, ListView
from utilities.data_gen import create_photo_list
from .models import Category, Photo

class GalleryView(ListView):
    template_name = "gallery.html"
    model = Photo
    context_object_name = "photos"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def get_queryset(self):
        category_name = self.request.GET.get("category")
        if category_name:
            photos = Photo.objects.filter(category__title=category_name)
        else:
            photos = Photo.objects.all()
        return photos

class PhotoDetailView(DetailView):
    template_name = "photo_details.html"
    model = Photo
    context_object_name = "photo"