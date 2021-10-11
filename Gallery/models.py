from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.title


def image_dir_path(instance, filename):
    return f"{slugify(instance.category.title)}/{filename}"

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    homepage = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, editable=False)
    image = models.ImageField(upload_to=image_dir_path)
    description = models.TextField(max_length=2000)
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Képek"

    def __str__(self):
        return self.title

def slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(slug_generator, sender=Photo)