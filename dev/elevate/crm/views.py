from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def home(request):

    return render(request, 'crm/index.html')

def all_tasks(request):

    # perform a DB query 
    query_data_all = Task.objects.all()
    context = { 'allTasks' : query_data_all }

    return render(request, 'crm/all-tasks.html', context)

def register(request):
    return render(request, 'crm/register.html')


def create_task(request):
    
    form = TaskForm()

    # check the request method
    if request.method == "POST":

        form = TaskForm(request.POST)
        # check if form data is valid
        if form.is_valid():
            # send data to database
            form.save()

            # redirect user to the task input page - uses the 'name' attribute in the urlspattern route
            return redirect('all-tasks')

    # create a context dictionary
    context = { 'form' : form }

    return render(request, 'crm/create-task.html', context)

def update_task(request, pk):

    # fetch a specific object by pk
    task = Task.objects.get(id=pk)

    # pre-populate the form with task attributes when rendered
    form = TaskForm(instance=task)

    if request.method == "POST":

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('all-tasks')

    context = { 'updateTask' : form }
    return render(request, 'crm/update-task.html', context)
    
def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":

        task.delete()

        return redirect('all-tasks')

    return render(request, 'crm/delete-task.html')