from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('explore/', views.explore, name='explore'),
    path('services/', views.services, name='services'),
    path('about-us/', views.about_us, name='about-us'),
]
