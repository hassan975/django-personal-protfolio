from django.db import models

class ProjectAbout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='portfolio/image',blank=True)
    InstaURL = models.URLField()
    Gmail=models.CharField(max_length=100)