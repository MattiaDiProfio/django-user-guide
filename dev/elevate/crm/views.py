from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

def home(request):

    return render(request, 'crm/index.html')

def all_tasks(request):

    # perform a DB query 
    query_data_all = Task.objects.all()
    context = { 'allTasks' : query_data_all }

    return render(request, 'crm/all-tasks.html', context)

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        # send request payload to database
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('login')

    context = { 'RegistrationForm' : form }

    return render(request, 'crm/register.html', context)

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

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():        
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(
                request, 
                username=username, 
                password=password
            )
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = { 'LoginForm' : form }
    return render(request, 'crm/login.html', context)

@login_required(login_url='login')
def dashboard(request):

    return render(request, 'crm/dashboard.html')

def logout(request):
    
    # expires user session currently login into dashboard
    auth.logout(request)

    return redirect("")