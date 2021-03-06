from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title
