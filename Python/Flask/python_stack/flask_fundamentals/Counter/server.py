from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)  
app.secret_key='secret'                   

@app.route('/')
def index():
    if session['count']>=0:
        session['count']+=1
    else:
        session['count']=0
    return render_template ('index.html')  

@app.route('/add2')
def add2():
    session['count']+=1
    return redirect ('/')

@app.route('/reset')
def reset():
    session['count']=0
    return redirect ('/')

app.run(debug=True)   