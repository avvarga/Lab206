from django.shortcuts import render, HttpResponse, redirect
import datetime

def index (request):
    return redirect ('/session_words')

def session_words (request):
    if not 'words' in request.session:
        request.session['words'] = []
    return render (request, 'index.html') 

def add (request):
    data = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'date': datetime.datetime.now().strftime(' %I:%M:%S%p, %B %d %Y '),
        'big': request.POST.get('big')
    }
    request.session['words'].append(data)
    request.session.modified = True
    print request.session['words']
    
    return redirect ('/session_words')

def clear (request):
    request.session.clear()
    return redirect ('/session_words')