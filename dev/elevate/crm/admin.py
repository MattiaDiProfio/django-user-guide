from django.contrib import admin

# Import the model we created
from .models import Task, Review

# Register models so we can read it in DAP
admin.site.register(Task)
admin.site.register(Review)