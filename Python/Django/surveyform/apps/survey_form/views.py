from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render (request, 'survey_form/index.html')

def process(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    request.session['data'] = request.POST,
    request.session['counter'] +=1
    return redirect ('/result')

def result(request):
    return render (request, 'survey_form/result.html')
