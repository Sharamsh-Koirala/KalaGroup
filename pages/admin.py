from django.contrib import admin

# Register your models here.
from .models import IndexPage, ServicePage, AboutPage

# Register your models here.
admin.site.register(IndexPage)
admin.site.register(ServicePage)
admin.site.register(AboutPage)