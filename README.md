# Working with Django



This documents serves as a personal guide to help developers gain confidence using the Django framework.
Throughout this guide, I have documented the steps necessary to setup, run and customize a Django application, and for each step I have included a short explaination to give you some context on what each step does.

## Set-up of a Django project
1. create a folder named "dev" on your desktop and travel to it through the command line
2. global pip-install virtualenv - a python package to create virtual environments 
3. create your custom virtual environment with the command virtualenv "your_env_name"
4. Activate your environment with the command "your_env_name"\Scripts\activate - now all packages installed are 
constricted to this virtual environment  - use "\" and not "/", if this works you should see your env name in brackets
5. deactivate it with the same but "deactivate"
6. within the venv, run pip install django
7. to create your django project, run the command django-admin startproject "project name"
8. finally open the "dev" folder via your editor of choice, I used VScode 

## How to run your server
1. travel to the folder with the same name as your project name 
2. run the command python manage.py runserver
3. you should be able to access your app on LOCALHOST or the port displayed in the cmd message " http://127.0.0.1:8000/"
4. paste that url in your browser and run it, you should see a django placeholder app (with a rocket animation)
5. stop the server with CTRL+C

## structure of a django project 
1. db.sqlite3 - a default sqlite database plugged into our app, good for dev but not for deployment 
2. manage.py - used to run admin tasks, control centre for the app, used for migrations etc.
3. inside the project folder 
    1. __init__.py - enforces the directory as a module 
    2. asgi.py - used for async development/actions
    3. settings.py - django config file for our project
    4. urls.py - store all the routes configured on our app (/home, /login, /dashboard etc.)
    5. wsgi.py - forwarding requests from web servers to a python web framework

## django apps

### concept 
    - django project is a collection of settings, configurations and apps
    - we can have one or multiple apps within a project
    - an app serves a unique purpose (microservices-like architecture, django projects are still monolithic though) such as a blog app where users can record their thoughts

### configuring a django app
1. run command django-admin startapp "app_name"
2. configure the app via settings.py - app "app_name" to the INSTALLED APPS 
3. migrate all files associated with the django default INSTALLED APPS to the app you just created with the command python manage.py migrate

### structure of a django app
1. admin.py - config file for our admin page, where we can carry out admin actions on our app
2. models.py - where we define models i.e. db tables in form of classes
3. views.py - set up business logic for app here 
4. init.py - same purpose as the above 
5. apps.py - info file about our app
6. test.py - carry out testing on the app (importan!!!)

## views and templates