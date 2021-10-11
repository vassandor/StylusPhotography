# Create your views here.
from django.views.generic import TemplateView, DetailView
from utilities.data_gen import create_photo_list
from .models import Category, Photo

class GalleryView(TemplateView):
    template_name = "gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context["images"] = Photo.objects.all()

        context["categories"] = Category.objects.all()
        return context

class PhotoDetailView(DetailView):
    template_name = "photo_details.html"
    model = Photo
    context_object_name = "photo"