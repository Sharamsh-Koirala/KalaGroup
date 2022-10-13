from django.shortcuts import render
from blogs.models import Blog
from subsidiaries.models import Subsidiary
from .models import IndexPage, ServicePage, AboutPage

def homepage(request):
    indexPage = IndexPage.objects.first()
    blogs = Blog.objects.all()[:4]
    subsidiaries = Subsidiary.objects.all()
    context = {'index': indexPage, 'blogs': blogs, 'subsidiaries': subsidiaries}
    return render(request, 'pages/index.html', context)


def about_us(request):
    aboutPage = AboutPage.objects.first()
    subsidiaries = Subsidiary.objects.all()
    context = {'about': aboutPage, 'subsidiaries': subsidiaries}
    return render(request, 'pages/about-us.html', context)


def services(request):
    servicePage = ServicePage.objects.first()
    context = {'service': servicePage}
    return render(request, 'pages/services.html', context)


def explore(request):
    return render(request, 'pages/explore.html')


def error_404_view(request, exception):
    return render(request, 'pages/404.html')