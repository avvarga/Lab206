from django.shortcuts import render, HttpResponse, redirect
def index (request):
    response = "Placeholder to later display the list of blogs"
    return HttpResponse(response)

def new (request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create (request):
    return redirect ('/')

def show (request,number):
    response = "Placeholder to display blog "+number
    return HttpResponse(response)

def edit (request, number):
    response = "placeholder to ediit blog "+number
    return HttpResponse(response)

def delete (request):
    return redirect ('/')