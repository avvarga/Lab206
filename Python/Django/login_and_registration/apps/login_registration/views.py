from django.shortcuts import render,redirect
from django.contrib import messages
from models import *
import bcrypt, re

# Create your views here.
def index(request):
    return render (request,'index.html')

def login(request):
    errors = User.objects.valid_login(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect ('/')
    else:
        request.session['user'] = User.objects.get(email=request.POST['email']).first_name
        return redirect ('/success')  

def register(request):
    errors = User.objects.valid_registration(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect ('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
        request.session['user'] = User.objects.last().first_name
        return redirect ('/success')

def success (request):
    return render (request, 'success.html')