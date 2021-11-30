from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog_view(request):
    blogs_object = Blog.objects.all()
    context = {
        'blogs': blogs_object
    }
    return render(request, 'blogs/blogs-view.html', context)


def blog_detail_view(request, slug=None):
    blog_object = None
    if slug is not None:
        blog_object = Blog.objects.get(slug=slug)

    context = {
        'object': blog_object
    }

    return render(request, 'blogs/detail.html', context=context)
