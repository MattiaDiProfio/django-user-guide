from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def home(request):

    # context dictionary to be passed to the index.html template
    context = {
        'name' : 'Mattia', 
        'age' : 21, 
        'numbers' : [1,3,6,2,7]
    }

    # pass context via the render function
    return render(request, 'crm/index.html', context)

def task(request):

    # perform a DB query 
    query_data_all = Task.objects.all()
    context = {
        'allTasks' : query_data_all
    }

    return render(request, 'crm/task.html', context)

def register(request):
    return render(request, 'crm/register.html')


def task_form(request):
    
    form = TaskForm()

    # create a context dictionary
    context = { 'form' : form }

    return render(request, 'crm/task-form.html', context)