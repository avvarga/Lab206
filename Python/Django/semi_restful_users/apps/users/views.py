from django.shortcuts import render, redirect
from models import *;

# Create your views here.
def index (request):
    return redirect ('/users')

def users (request):
    print User.objects.all()
    return render (request, 'index.html', {'users': User.objects.all()})

def new (request):
    return render (request, 'new.html')

def create (request):
    User.objects.create(name = request.POST['name'], email = request.POST['email'])
    return redirect ('/')

def show (request,id):
    return render (request, 'show.html', {'users': User.objects.get(id=id)})

def edit (request,id):
    return render (request, 'edit.html', {'users': id})

def update (request):
    current = User.objects.get(id=request.POST['id'])
    current.name = request.POST['name']
    current.email = request.POST['email']
    current.save()
    return redirect ('/users/'+request.POST['id'])

def destroy (request,id):
    current = User.objects.get(id=id)
    current.delete()
    return redirect ('/') 
