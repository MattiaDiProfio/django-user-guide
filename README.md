# Working with Django

<a id="table-of-contents"></a>
# Table of Contents

- [Django projects](#django-projects)
  - [Environment setup](#environment-setup)
  - [Manage the server](#manage-the-server)
  - [Structure of a project](#project-structure)
- [Django apps](#django-apps)
  - [What are Django apps?](#what-are-django-apps)
  - [Configuring an app](#configure-django-app)
  - [Structure of an app](#structure-of-django-app)
- [View and Templates](#views-templates)
  - [What are views?](#what-are-views)
- [Credits](#credits)

This documents serves as a personal guide to help developers gain confidence using the Django framework.
Throughout this guide, I have documented the steps necessary to setup, run and customize a Django application, and for each step I have included a short explaination to give you more context on how the process works.

<a id="django-projects"></a>
# Django projects
[back to top](#table-of-contents)

<a id="environment-setup"></a>
## Environment setup

1. create a folder named "dev" on your desktop and travel to it through the command line
2. global pip-install virtualenv - a python package to create virtual environments
3. create your custom virtual environment with the command virtualenv "your_env_name"
4. Activate your environment with the command "your_env_name"\Scripts\activate - now all packages installed are
constricted to this virtual environment  - use "\" and not "/", if this works you should see your env name in brackets
5. deactivate it with the same but "deactivate"
6. within the venv, run pip install django
7. to create your django project, run the command django-admin startproject "project name"
8. finally open the "dev" folder via your editor of choice, I used VScode

<a id="manage-the-server"></a>
## Manage the server

1. travel to the folder with the same name as your project name
2. run the command python manage.py runserver
3. you should be able to access your app on LOCALHOST or the port displayed in the cmd message " <http://127.0.0.1:8000/>"
4. paste that url in your browser and run it, you should see a django placeholder app (with a rocket animation)
5. stop the server with CTRL+C

<a id="project-structure"></a>
## Structure of a Django project

1. db.sqlite3 - a default sqlite database plugged into our app, good for dev but not for deployment
2. manage.py - used to run admin tasks, control centre for the app, used for migrations etc.
3. inside the project folder
    1. __init__.py - enforces the directory as a module
    2. asgi.py - used for async development/actions
    3. settings.py - django config file for our project
    4. urls.py - store all the routes configured on our app (/home, /login, /dashboard etc.)
    5. wsgi.py - forwarding requests from web servers to a python web framework

<a id="django-apps"></a>
# Django apps
[back to top](#table-of-contents)

<a id="what-are-django-apps"></a>
## What are Django apps?

- django project is a collection of settings, configurations and apps
- we can have one or multiple apps within a project
- an app serves a unique purpose (microservices-like architecture, django projects are still monolithic though) such as a blog app where users can record their thoughts

<a id="configure-django-app"></a>
## Configuring a Django app

1. run command django-admin startapp "app_name"
2. configure the app via settings.py - app "app_name" to the INSTALLED APPS
3. migrate all files associated with the django default INSTALLED APPS to the app you just created with the command python manage.py migrate

<a id="structure-of-django-app"></a>
## Structure of a Django app

1. admin.py - config file for our admin page, where we can carry out admin actions on our app
2. models.py - where we define models i.e. db tables in form of classes
3. views.py - set up business logic for app here
4. init.py - same purpose as the above
5. apps.py - info file about our app
6. test.py - carry out testing on the app (importan!!!)

<a id="views-templates"></a>
# View and Templates
[back to top](#table-of-contents)

<a id="what-are-views"></a>
## What are Views?

- views are python functions or classes used to respond to a particular request

<a id="setup-webpage"></a>
## Setup a starting webpage 

steps to be taken are
1. import path from django.urls and HttpResponse from django.http 
2. define a view via the function with name of "route" such as register(request) which returns an HttpResponse message 
3. create a urlpatterns list to encapsulate all urls used in the application
- enter path(routename, view to be returned)
- i.e. urlpatterns = [path('route_name', 'view_name' - same name of function defined in step 2)]

<a id="credits"></a>
# Credits
[back to top](#table-of-contents)

The material for this document has been gathered while studying the course *Python Django - Ultimate beginners course* on Udemy, authored by Arno Pretorius.