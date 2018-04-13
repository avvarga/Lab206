from django.shortcuts import render, redirect
import datetime, random

def index (request):
    if not 'result' in request.session:
        request.session['result'] = 0
    if not 'log' in request.session:
        request.session['log'] = []
    return render (request, 'ninjaGold/index.html')

def process_money (request):
    if request.POST['building'] == 'farm':
        gold = random.randrange(10,21)
    elif request.POST['building'] == 'cave':
        gold = random.randrange(5,11)
    elif request.POST['building'] == 'house':
        gold = random.randrange(2,6)
    elif request.POST['building'] == 'casino':
        gold = random.randrange(-50,51)
    if gold >0:
        data = {
            'message': "Earned {} gold at the {}. ({:%Y/%m/%d %I:%M %p})".format(gold,request.POST['building'],datetime.datetime.now()),
            'color': 'green'
        }
        request.session['log'].insert(0,data)
        request.session.modified = True
    elif gold <0:
        temp = 0-gold
        data = {
            'message': "Lost {} gold at the {}. ({:%Y/%m/%d %I:%M %p})".format(temp,request.POST['building'],datetime.datetime.now()),
            'color': 'red'
        }
        request.session['log'].insert(0,data)
        request.session.modified = True
    request.session['result']+=gold
    print request.session['log']
    return redirect ('/')

def reset (request):
    request.session.clear()
    return redirect ('/')