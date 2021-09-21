# Create your views here.
from django.views.generic import TemplateView
from utilities.data_gen import create_photo_list

class GalleryView(TemplateView):
    template_name = "gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context["images"] = create_photo_list(21)
        return context