from django.forms import ModelForm
from .models import Task

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# create a form model based on the Task model found in models.py
# this model form allows users to add a new task using a form
class TaskForm(ModelForm):

    # define class metadata 
    class Meta:
        model = Task
        # specify attributes of Task model we want to utilise 
        fields = '__all__' # utilise all APPLICABLE attributes 

# create django class to define new app user
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        # cherry-pick the user attributes we want to define
        fields = ['username', 'email', 'password1', 'password2']

# create django class to instantiate login form model
class LoginForm(AuthenticationForm):

    # fields to enter data 
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())