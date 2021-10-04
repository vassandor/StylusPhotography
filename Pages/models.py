from django.db import models

# Create your models here.

class PageInfo(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    instagram = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Oldal info"

    def __str__(self):
        return f"{self.title}: {self.subtitle}"

class HomePage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name_plural = "Home page info"

    def __str__(self):
        return self.title

class AboutPage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name_plural = "About page info"

    def __str__(self):
        return self.title