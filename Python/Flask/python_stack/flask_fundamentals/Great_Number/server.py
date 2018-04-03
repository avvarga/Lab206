from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key='secret'                   

@app.route('/')
def index():
    if not isinstance (session['random'],int):
        session['random']=random.randrange(0,101)
    return render_template ('index.html')  

@app.route('/submit', methods=['POST'])
def submit():
    if str(session['random']) == request.form['number']:
        session['result'] = "That's right!"
    elif str(session['random']) > request.form['number']:
        session['result'] =  "Too low!"
    else:
        session['result'] =  "Too high!"
    return redirect ('/')

app.run(debug=True)   