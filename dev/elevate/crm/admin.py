from django.contrib import admin

# Import the model we created
from .models import Task

# Register task so we can read it in DAP
admin.site.register(Task)