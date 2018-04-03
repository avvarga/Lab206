from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)  
app.secret_key='secret'                   

@app.route('/')
def index():
    if not 'result' in session:
        session['result']=0
        session['log']=[]
    return render_template ('index.html') 

@app.route('/process_money', methods = ['POST'])
def process_money():
    if request.form['building'] == 'farm':
        gain = random.randrange(10,21)
        session['result'] += gain
        session['log'].append ("Earned "+str(gain)+ " gold from the farm. {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
    if request.form['building'] == 'cave':
        gain = random.randrange(5,11)
        session['result'] += gain
        session['log'].append ("Earned "+str(gain)+ " gold from the cave. {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
    if request.form['building'] == 'house':
        gain = random.randrange(2,6)
        session['result'] += gain
        session['log'].append ("Earned "+str(gain)+ " gold from the house. {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
    if request.form['building'] == 'casino':
        gain = random.randrange(-50,51)
        session['result'] += gain
        if gain >0:
            session['log'].append("Earned "+str(gain)+ " gold at the casino. {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
        elif gain <0:
            session['log'].append("Lost "+str(gain)+ " gold at the casino. {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
    return redirect ('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect ('/')

app.run(debug=True)   