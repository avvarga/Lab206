from django.shortcuts import render,redirect
from django.contrib import messages
from models import *
# Create your views here.

def index (request):
    return render (request, 'index.html', {'courses': Course.objects.all()})

def remove (request,id):
    return render (request, 'confirmation.html', {'courses': Course.objects.get(id=id)})

def add (request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
             messages.error(request, error)

    else:
        Course.objects.create(name = request.POST['name'], desc = request.POST['description'])
    return redirect ('/')

def destroy (request,id):
    current = Course.objects.get(id=id)
    current.delete()
    return redirect ('/') 