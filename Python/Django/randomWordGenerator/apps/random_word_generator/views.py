from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index (request):
    return redirect('/random_word')

def random_word (request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    return render(request,'random_word_generator/index.html')

def generate (request):        
    request.session['counter'] += 1
    request.session ['word'] = get_random_string(length=14)
    return redirect ('/random_word')

def reset (request):
    request.session.clear()
    return redirect ('/random_word')
