from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    # save a timestamp of when an instance of Task was created
    created = models.DateTimeField(auto_now_add=True)