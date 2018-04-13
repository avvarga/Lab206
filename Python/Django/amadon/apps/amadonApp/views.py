from django.shortcuts import render, redirect

def index(request):
    return redirect ('/amadon')

def amadon(request):
    if not 'units' in request.session:
        request.session['units'] = 0
    if not 'total' in request.session:
        request.session['total'] = 0
    else:
        print request.session['item']
    return render (request, 'index.html')

def buy(request):
    for items in request.session['item']:
        if items['id'] == int(request.POST['items_id']):
            request.session['order'] = items['price']*int(request.POST['quantity'])
            request.session['units'] += int(request.POST['quantity'])
            request.session['total'] += request.session['order']
    return redirect ('/amadon/checkout')

def checkout(request):
    return render(request, 'checkout.html')

def reset(request):
    request.session['total'].clear()
    request.session['units'].clear()
    return redirect ('/amadon')
















        #     a={
        #     'item': 'Dojo Tshirt',
        #     'price': 19.99,
        #     'id': 1
        # }
        # b={
        #     'item': 'Dojo Sweater',
        #     'price': 29.99,
        #     'id': 2
        # }
        # c={
        #     'item': 'Dojo Cup',
        #     'price': 4.99,
        #     'id': 3
        # }
        # d={
        #     'item': 'Algorithm Book',
        #     'price': 49.99,
        #     'id': 4
        # }
        # request.session['item'].append(a)
        # request.session.modified = True