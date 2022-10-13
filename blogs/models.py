from email.policy import default
from django.db import models
import uuid
from tinymce.models import HTMLField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default='default.jpg')
    ending_image = models.ImageField(null=True, blank=True, default='default.jpg')
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
