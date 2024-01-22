from django.urls import path
from . import views # import any function in the views.py file

urlpatterns = [
    path('', views.home), 
    # define response path for the 'register' route 
    path('register', views.register), 
    # define response path for the 'task' route 
    path('task', views.task), 
]