from django.shortcuts import render, HttpRequest, redirect

def index():

    return render (request, 'time_display/index.html')

# Create your views here.
