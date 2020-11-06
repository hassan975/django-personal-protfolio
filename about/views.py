from django.shortcuts import render
from .models import ProjectAbout

def about(request):
    projects=ProjectAbout.objects.all()
    return render(request,'about/aboutme.html',{'projects':projects})