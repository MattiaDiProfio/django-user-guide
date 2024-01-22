# Working with Django

<a id="table-of-contents"></a>

## Table of Contents

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
    - [Setup basic webpage](#setup-webpage)
  - [What are templates?](#what-are-templates)
  - [Django Templating Language](#django-templating-language)
- [Integrate a database](#integrate-database)
  - [Django Admin Panel](#django-admin-panel)
  - [Django models](#django-models)
  - [Perform database queries](#db-queries)
- [Credits](#credits)

This document serves as a personal guide to help developers understand the basics of working with the Django framework.
Throughout this guide, I have documented the steps necessary to setup, run and customize a Django application, and for each step I have included a short explaination to give you more context on how the process works.

<a id="django-projects"></a>

## Django projects

[back to top](#table-of-contents)

<a id="environment-setup"></a>

### Environment setup

First of all, we have to setup our development environment for our Django project. This can be done by following these steps on windows (for Mac it should be similar).

- create a folder named "dev" on your desktop and travel to it through the cmd
- run the command `pip install virtualenv` to install a package for declaring virtual environments

Now let's work with virtual environments

- Create your custom virtual environment with the command `virtualenv <your_env_name>`
- Activate your environment with the command `your_env_name\Scripts\activate`. Now all packages installed are constricted to this virtual environment.
- To deactivate the virtual environment run the command `your_env_name\Scripts\deactivate`

Finally, let's install Django

- Within the virtual environment folder in the cmd, run the command  `pip install django`
- To create your django project, run the command `django-admin startproject <project_name>`
- Finally, open the *dev* folder via your editor of choice, I used VScode

<a id="manage-the-server"></a>

### Manage the server

Throughout the development of your Django project, you will have manage the status of your local server. Here is how you can do it.

- Travel to the folder with the same name as your project name
- Run the command `python manage.py runserver`
- You should be able to access your app on LOCALHOST or the port displayed in the cmd message `...http://127.0.0.1:8000/`
- Paste that url in your browser and run it, you should see a django placeholder app (with a rocket animation)
- Stop the server with by hitting `CTRL+C` in the cmd

<a id="project-structure"></a>

### Structure of a Django project

After successfully creating your Django project and opening it via your editor of choice, you should familiarise yourself with the file structure below.

- *db.sqlite3* - a default sqlite database plugged into our app
- *manage.py* - used to run admin tasks, a control centre for the app
- Inside the project folder named *<project_name>*
  1. *__init__.py* - ensures python treats this directory as a module
  2. *asgi.py* - used for async development and actions
  3. *settings.py* - Django config file for our project
  4. *urls.py* - store all the routes configured on our app (/home, /login, /dashboard etc.)
  5. *wsgi.py* - used forwarding requests from web servers to a python web framework

<a id="django-apps"></a>

## Django apps

[back to top](#table-of-contents)

<a id="what-are-django-apps"></a>

### What are Django apps?

A Django project is a collection of settings, configurations and apps and we can have one or multiple apps within a project.
A Django app serves a unique purpose (microservices-like architecture, altough django projects are still monolithic) such as a blog app where users can record their thoughts.

<a id="configure-django-app"></a>

### Configuring a Django app

To configure a Django app within your project, follow the steps below.

- Run command `django-admin startapp <app_name>`

- Configure the app via the *settings.py* file in your project folder by adding the entry *<your_app_name>* into the *INSTALLED_APPS* list.

- Migrate all files associated with the Django default INSTALLED_APPS to the app you just created by running the command `python manage.py migrate`

<a id="structure-of-django-app"></a>

### Structure of a Django app

Once you have successfully created your Django app, you should be able to recognise the file tree described below.

- *admin.py* - config file for our admin page, where we can carry out admin actions on our app
- *models.py* - where we define models, such as DB tables defined with python classes
- *views.py* - where we setup the business logic for our app
- *init.py* - ensures this folder is treated like a python module
- *apps.py* - information file about our application
- *test.py* - where we can carryout testing for our Django app - **important!**

<a id="views-templates"></a>

## View and Templates

[back to top](#table-of-contents)

<a id="what-are-views"></a>

### What are Views?

Views are python functions or classes used to respond to a particular request.

<a id="setup-webpage"></a>

### Setup a starting webpage

Now that you have your Django project and app setup, let's look at the steps necessary to create a basic request-response cycle.

- Define a *urls.py* file in the crm folder or your project folder

Inside the newly created file:

- Write the lines `import path from django.urls` and `import HttpResponse from django.http`
- Inside the *views.py* file define a View in the urls.py file, via a function with name of *"route"*, such as `def register(request)` which returns an HttpResponse message.
- Create a *urlpatterns* list to encapsulate all urls used in the application
- Enter the line `path(routename, view_to_return)` in urls.py file, i.e. `urlpatterns = [path('route_name', 'view_name')]`

- Within the same file run the line `from django.urls import include` link the app's urls.py to the projects urls.py
- Within the `urlpatterns` list, add a path with empty route and view, such as `path('', include('projectname.urls')`
- To setup the app's *views.py* and *urls.py*
  1. Run the import `from . import views` in the *urls.py* file
  2. Add the following path to urlpatterns list - `path('register', views.register),`
- To configure the default page for our app
  1. In *urls.py*, define an empty `path('', views.home_view)`
  2. In *views.py* define a function or View for the home page

<a id="what-are-templates"></a>

### What are templates?

Templates are structured files written using Django templating language (DTL) and allow different webpages to share the same structure, but with customizable content

To configure templates in your app:

- Travel to you app folder, create a "templates" folder and within that create a folder called "app_name" to avoid namespace issues
- Within the last created folder, create a *home.html* template file and add some basic markup
- In the *views.py* file, call the render function within the View/function for the homepage - `render(request, 'crm/index.html')`, now the template is rendered when user hits that route

Template inheritance allows you to define components in a parent template that children template can use, without redefining it themselves
Elements are components of a template which can be *reused* - such as button, or a headers

Template inheritance can be setup with the following steps

- Create a base template in templates/app_name - i.e. base.html
- Define a unique space for this template with `{% block content %} custom data here {% endblock %}` - everything outside this block will be inherited by child templates
- Link this parent template by going to any other template and doing the following
  1. Add this line at the very top of the template `{% extends "crm/base.html" %}`
  2. Wrap the content you want to display on a child template with the `{% block content %} custom data here {% endblock %}` operator

<a id="django-templating-language"></a>

### Django Templating Language

- DTL is a mini language to write logic within our templates and render data through your templates, using data passed to the template via the views in views.py for example
- You can pass data to your template by

1. Passing a dictionary as the 3rd parameter of the render function for the template you are trying to populate
2. Within the template, declare `{{ key_name }}` anywhere you wanna display the data associated with the *key_name* key in the dictionary you passed to the template
3. You can enforce conditional rendering with the following syntax `{% if condition %} content A {% else %} content B {% endif %}`
4. Similarly, you can loop over data using a for-loop like syntax `{% for n in list_to_iterate %} <p> {{ n }} </p> {% endfor %}`

<a id="integrate-database"></a>

## Integrating a Database

- Django apps come with a built-in SQLite relational database. Throughout this section, we will go through the steps to carry out CRUD operations on this database.

<a id="django-admin-panel"></a>

### Django admin panel

- The Django Admin Panel can be accessed by running your server and visiting the /admin route. The DAP allows you to manage the underlying SQLite database that comes with your app. To access the DAP, you will need login credentials, which can be accessed with the following steps:

1. Run the command `python manage.py createsuperuser`
2. Fill in the prompts as you go along, careful to type matching passwords as they won't be displayed on screen.
3. Re-start your server and login.

<a id="django-models"></a>

### Django models

- Django models are a feature used by Django to create tables along with their fields. Think of these as classes which represent database tables.

To create a model in Django, use the following steps:

1. Head over to *models.py* and declare a model with the following syntax `class Name(models.Model): your_fields` - make sure to consult the different datatypes allowed by Django [here](#https://www.freecodecamp.org/news/common-django-model-fields-and-their-use-cases/)
2. Migrate your created model by running the command `python manage.py makemigrations` in your cmd
3. Push the model to your database by running the command `python manage.py migrate`

After you declared your Django model, we got to register it on our Django app using the DAP. Follow these steps.

1. Open the *admin.py* file
2. Run the line `from .models import Name`
3. Run the line `admin.site.register(Name)` to register the model on the DAP
4. Login into the DAP, and you should see the Model registered as Name(s)

Now we have a look at how we can link multiple models using the concept of foreign keys.

1. Open the *models.py* and create a second model which you will link to an existing one.
2. Write the following line as an attribute to the newly created model `model_linked_name = modelsForeignKey(model_linked_name, on_delete=models.CASCADE)` - models.CASCADE ensures that all connections to a model are deleted once that particular instance is deleted.
3. Migrate and register this model as done with the previous one

<a id="db-queries"></a>

### Performing database queries

- ORM (Object relational mapping) is used to perform Django database queries. Follow the steps below to run a simple query to the Django SQLite database.

1. In the *views.py* file, run the following line `from .models import Model_name`
2. Inside the function/view you want to execute the query in, run the following line `query_data_all = Model_name.objects.all()` - this example fetches all the instances of the Model_name class
3. Pass the query results to your template via a context dictionary and render it onto your view.
4. **NOTE** - please google to find the appropriate query method to complete your task.

<a id="credits"></a>
# Credits
[back to top](#table-of-contents)

The material for this document has been gathered while studying the course *Python Django - Ultimate beginners course* on Udemy, authored by Arno Pretorius.