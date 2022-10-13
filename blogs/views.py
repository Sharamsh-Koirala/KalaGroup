from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request,pk):
    blogObj = Blog.objects.get(id=pk)
    context = {'blog':blogObj}
    return render(request, 'blogs/single-blog.html',context)