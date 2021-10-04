from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.title

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    visible = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField(max_length=2000)
    uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, blank=True)