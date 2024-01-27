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
- [Model forms and CRUD operations](#model-forms-crud)
  - [Create a model form](#create-model-form)
  - [Add CRUD functionalities](#crud-operations)
- [Configure static files](#static-files)
- [User authentication and authorization](#user-auth)
  - [Create new app user](#create-a-new-user)
  - [Configure user auth](#user-authentication)
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

[back to top](#table-of-contents)

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
4. __NOTE__ - please google to find the appropriate query method to complete your task.

<a id="model-forms-crud"></a>

## Model Forms and CRUDS

[back to top](#table-of-contents)

- A Model Form is a class used to convert a Django model into a Django form. This form can then be rendered on the front-end to collect user input.

<a id="create-model-form"></a>

### Create a Model Form

- To create a Model Form follow these steps:

1. Inside your app forlder, create the *forms.py* file.
2. Run the line `from django.forms import ModelForm`, this class is the 'parent' class which every form you create will inherit from.
3. Run the line `from .models import <model>` - model comes from models.py
4. Define the model form class with the following syntax `class <model>Form(ModelForm): class Meta: model = <model> fields = '__all__'` - the Meta class allows us to specify which model and which model attributes the Form will model.
5. Define a template for the form we just defined :

- Inside *templates/<app_name>* create a .html file and populate it accordingly
- Inside the *views.py* file, we must setup the View to be rendered (see above for a refresher) and then connect this View inside the *urls.py* file.

6. Now we must create the View to be rendered:

- Run the line `from .forms import <model>Form` inside the *views.py* file
- Inside the last View function you defined, instantiate the class you just imported
- create a context dictionary `{ "form" : instance_created }` and return `render(...)` as done with other views.
- Finally, go to the last .html file you created and populate it to display the form model you passed in as a context dictionary. Here is an example below :
`<form method="POST" autocomplete="off" enctype="multipart/form-data" {% csrf_token %} {{ form.as_p }} <input type="submit" value="Submit"> </form>` - as_p helps with formatting and labels of attribute names

<a id="crud-operations"></a>

### Adding CRUD operations

1. **C - CREATE**

- To create a new model instance, follow the steps outlined below.

1. Go to the *views.py* file, and define a view/function named `def create_<model_instance>(request): pass` if not there already
2. Import the `redirect` method from the `django.shortcuts` package
3. Inside the method defined in step 1 :
  
- Check what the form action is with `if request.method == "POST"`
- If that's the case, reassign the form with `form = TaskForm(request.POST)`
- Then we check if the form data is valid with `if form.is_valid():`
- If the data is valid we save the object and redirect the user to the input page which triggered the CREATE action - `form.save() return redirect('task')`
- if the request method is not POST, simply `return render(...)`

2. **R - READ**

- To read a model instance from the database using an instance id for example, follow the steps outlined below.
- If you would like to get all instances from the database, use the `.all()` method to query, otherwise use the `.get(id=...)` method to fetch an object based on its creation id.

3. **U - UPDATE**

- To update an existing model instance, follow the steps outlined below.

1. create a new View called `update-<model>.html` and populate it with the `base.html` components and a title to distinguish it.
2. Set up your view in `views.py` and add the url to urlpatterns in `urls.py`.

- Note that to make a url __dynamic__ we use the following format `path('url/<str:pk>',...),`
- Similarly, the view you just declared takes in *request* and *pk* as parameters.
- Inside the view you defined, follow a similar process to the one in the __CREATE__ section above:

  1. fetch the object from the database based on pk input - `obj = <Model>.objects.get(id=pk)`
  2. define a form object `form = <Model>Form(instance=obj)`
  3. check if the method is POST, if it is `form = <Model>Form(request.post, instance=task)`
  4. check if the form data is valid, if it is then save and redirect.
  5. Inline with the POST if statement, define a context dictionary with the form defined and return `render(request, view_name, context)`

- In order to allow users to access the edit page of a particular object, we can use a link tag on the frontend which directs the user to the page for that specific object, for example `<a href = "{% url 'update-task' task.id %}"> Update task </a>` is displayed on the `all-tasks.html` page using a for loop.
- Finally, update the data loaded in the field and it should update it.

4. **D - DELETE**

- create a template called `delete-<model>.html`, then add connect `base.html` and add the following form inside `<form method="POST" autocomplete="off" enctype="multipart/form-data" {% csrf_token %} <input type="submit" value="Delete"> </form>`
- set up functionality in *views.py* with a dynamic-url view and connect it to *urls.py*
- to delete the task given the `pk` id, simply check if the form method is POST and then fetch the object with `<Model>.objects.get(id=pk)` and then delete it with `<obj>.delete()`.
- redirect the user after operation

<a id="static-files"></a>

## Static files

[back to top](#table-of-contents)

- Static files such as css and JS files remain unchanged during a website's operation. They are directly sent to the user's web browser without being modified.
- To configure any static file, follow the process below.

1. create a `static` folder in the project root directory
2. in your app's *settings.py* files, type the following after the STATIC_URL variable - `STATICFILES_DIRS = [ BASE_DIR / 'static' ]` to let django know where to find our static files.
3. create `css` and `js` subfolders in the `static` folder, to house our static css and Javascript files.
4. create a `style.css` file in the css folder, and write some code for testing purposes.
5. to connect your static files to the frontend, write `{% load static %}` at the very top of your app's `base.html` file.
6. To connect your css static files, define a `head` tag in your `base.html` and within that, the following tag `<link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">`
7. Similarly, create an `app.js` file in static/js and use a `script` tag to connect the static javascript files `<script src="{% static 'js/app.js' %}"></script>`

<a id="static-files"></a>

## User Authentication & Authorization

- User Authentication is concerned with ensuring that login/signup procedures work as intended for registering and returning app users. User Authrorization is concered with what a logged in user can and cannot do on the application. To setup user auth in your app, follow the steps below.

<a id="create-a-new-user"></a>

### Create a new user

1. Inside *forms.py* import the following `from django.contrib.auth.forms import UserCreationForm`, followed by the default User model import `from django.contrib.auth.models import User`
2. Define a new class `CreateUserForm(UserCreationForm):` and within this class define the `Meta` class, where you can cherrypick the fields which will make up the User objects.
3. Inside the *views.py* file, import the class you just defined, then within the `register` view
  
  - Create a `form` variable to instantiate the class imported.
  - Check if the form method is POST and the form data is valid, in which case save the form and return an HttpResponse with a suitable message.
  - Create the context dictionary `context = { 'RegistrationForm' : form }` and pass it to the `render(...)` method.
  - Inside the `register.html` template, define the basic form syntax to send POST requests in django
  - Within the form, under the csrf token, type `{{ RegistrationForm.as_p }}` to display the registration form.

<a id="user-authentication"></a>

### User authentication

[back to top](#user-auth)

- To setup user authentication, follow the steps below. We assume you have completed all the above steps up to this point.

1. Create a *login.html* and a *dashboard.html* file in the templates/crm folder
2. Populate the *login.html* template with the same contents as *register.html* and remove all unrelated code, then populate the *dashboard.html* page with basic text
3. Next, we configure the *views.py* and *urls.py* files in the same way done before.
4. In the *forms.py* file, import `AuthenticationForm` from `django.contrib.auth.forms` and `from django import forms` and `from django.forms.widgets import PasswordInput, TextInput`
5. Still in *forms.py*, create a LoginForm class which inherits the `AuthenticationForm` class, as set the its attributes as follows :

- `username = forms.CharField(widget=TextInput())`
- `password = forms.CharField(widget=PasswordInput())`

6. Inside *views.py* import the LoginForm model class just declared and instantiate it within the login view declared before. 

- check for the POST method and if that's the case assign `form = LoginForm(request.POST, data=request.POST)`.
- run the following at the top of *views.py* - `from django.contrib.auth.models import auth` and `from django.contrib.auth import authenticate, login, logout`
- Now we check if the form input matches a record in the data, and either login the user or prompt them to try again. An example of the full login view/function is provided.
`
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
`

7. Finally, we populate the *login.html* file with `{{ LoginForm.as_p }}` and add a login url in the *base.html* file.
8. Modify the register view so that the user is redirected to the login url when they register a new account

# Credits

[back to top](#table-of-contents)

The material for this document has been gathered while studying the course *Python Django - Ultimate beginners course* on Udemy, authored by Arno Pretorius.
