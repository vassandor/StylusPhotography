import os, time, shutil

from PIL import Image
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_delete

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
    description = models.TextField(max_length=2000, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.replace_image()
        super(Photo, self).save(*args, **kwargs)
        self.resize_image()

    def resize_image(self):
        image_path = self.image.path
        img = Image.open(image_path)
        max_size = 1500
        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    def replace_image(self):
        try:
            photo = Photo.objects.get(id=self.id)
            if photo.image.name != self.image.name:
                photo.image.delete(save=False)
        except:
            pass

    class Meta:
        verbose_name_plural = "Képek"

    def __str__(self):
        return self.title if self.title else self.image.name

def slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        slug = f"{slugify(instance.category)}-{slugify(instance.title)}"
        if Photo.objects.filter(slug=slug).exists():
            slug += f"-{int(time.time())}"
        instance.slug = slug

pre_save.connect(slug_generator, sender=Photo)

def image_cleanup(sender, instance, **kwargs):
    if os.path.exists(instance.image.path):
        image_folder = os.path.dirname(instance.image.path)
        os.remove(instance.image.path)
        if not os.listdir(image_folder):
            shutil.rmtree(image_folder, ignore_errors=True)

post_delete.connect(image_cleanup, sender=Photo)