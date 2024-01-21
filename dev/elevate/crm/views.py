from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    # context dictionary to be passed to the index.html template
    context = {
        'name' : 'Mattia', 
        'age' : 21, 
        'numbers' : [1,3,6,2,7]
    }

    # pass context via the render function
    return render(request, 'crm/index.html', context)

def register(request):
    return render(request, 'crm/register.html')
