from django.urls import path
from . import views # import any function in the views.py file

urlpatterns = [
    path('', views.home, name=""), 

    # define response path for the 'register' route 
    path('register', views.register, name="register"), 

    # define response path for the 'task' route 
    path('task', views.task, name="task"), 

    # define response path for the 'task' model form
    path('task-form', views.task_form, name="task-form"),
]