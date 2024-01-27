from django.urls import path
from . import views # import any function in the views.py file

urlpatterns = [
    path('', views.home, name=""), 

    path('register', views.register, name="register"), 

    path('all-tasks', views.all_tasks, name="all-tasks"), 

    path('create-task', views.create_task, name="create-task"),

    # dynamic url which renders the page based on the task id passed
    path('update-task/<str:pk>', views.update_task, name="update-task"),

    path('delete-task/<str:pk>', views.delete_task, name="delete-task"),
]