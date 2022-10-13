from django.db import models
import uuid
from tinymce.models import HTMLField
# Create your models here.

class IndexPage(models.Model):
    title = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200,null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default='default.jpg')
    gallery_photo1 = models.ImageField(null=True, blank=True)
    gallery_photo2 = models.ImageField(null=True, blank=True)
    gallery_photo3 = models.ImageField(null=True, blank=True)
    gallery_photo4 = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        img = ''
        try:
            if self.feature_image.url:
                img = self.feature_image.url
        except:
            img = ''
        return img 

class ServicePage(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default='default.jpg')
    gallery_photo1 = models.ImageField(null=True, blank=True)
    gallery_photo2 = models.ImageField(null=True, blank=True)
    gallery_photo3 = models.ImageField(null=True, blank=True)
    gallery_photo4 = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        img = ''
        try:
            if self.feature_image.url:
                img = self.feature_image.url
        except:
            img = ''
        return img 

class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default='default.jpg')
    gallery_photo1 = models.ImageField(null=True, blank=True)
    gallery_photo2 = models.ImageField(null=True, blank=True)
    gallery_photo3 = models.ImageField(null=True, blank=True)
    gallery_photo4 = models.ImageField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        img = ''
        try:
            if self.feature_image.url:
                img = self.feature_image.url
        except:
            img = ''
        return img 