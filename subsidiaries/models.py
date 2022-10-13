from email.policy import default
from django.db import models
import uuid
from tinymce.models import HTMLField
# Create your models here.

class Subsidiary(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default='default.jpg')
    gallery1 = models.ImageField(null=True, blank=True)
    gallery2 = models.ImageField(null=True, blank=True)
    gallery3 = models.ImageField(null=True, blank=True)
    gallery4 = models.ImageField(null=True, blank=True)
    gallery5 = models.ImageField(null=True, blank=True)
    teamMemberName1 = models.CharField(max_length=200)
    teamMemberPhoto1 =models.ImageField(null=True, blank=True)
    teamMemberName2 = models.CharField(max_length=200)
    teamMemberPhoto2 =models.ImageField(null=True, blank=True)
    teamMemberName3 = models.CharField(max_length=200)
    teamMemberPhoto3 =models.ImageField(null=True, blank=True)
    teamMemberName4 = models.CharField(max_length=200)
    teamMemberPhoto4 =models.ImageField(null=True, blank=True) 
    services = HTMLField(null=True, blank=True)
    created = models.DateField(auto_now_add=False, null=False, blank=False)
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
