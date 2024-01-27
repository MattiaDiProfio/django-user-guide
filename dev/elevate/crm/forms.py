from django.forms import ModelForm
from .models import Task

# create a form model based on the Task model found in models.py
# this model form allows users to add a new task using a form
class TaskForm(ModelForm):

    # define class metadata 
    class Meta:
        model = Task
        # specify attributes of Task model we want to utilise 
        fields = '__all__' # utilise all APPLICABLE attributes 

    