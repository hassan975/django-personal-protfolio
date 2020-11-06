from django.shortcuts import render, get_object_or_404
from .models import Projects


def all_blogs(request):
    blogs = Projects.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blogs = get_object_or_404(Projects, pk=blog_id)
    return render(request, 'blog/detail.html', {'blogs': blogs})
