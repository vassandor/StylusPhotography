from utilities.data_gen import create_photo_list
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class AboutView(TemplateView):
    template_name = "about.html"

class GalleryView(TemplateView):
    template_name = "gallery.html"
    
    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context["images"] = create_photo_list(21)
        return context