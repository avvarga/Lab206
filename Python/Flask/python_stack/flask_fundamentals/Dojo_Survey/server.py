from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)                     
app.secret_key='secret'                   
                                 
@app.route('/')
def index():                                  
    return render_template ('index.html')  

@app.route('/process', methods=['POST'])
def process():
    counter =""
    if len(request.form['name']) < 1:
        counter +="name"
    elif len(request.form['comment']) < 1:
        counter +="comment"
    elif len(request.form['comment']) > 120:
        flash("Comment cannot be over 120 characters!")
        return redirect ('/')
    if len(counter) >0:
        flash("{} cannot be blank!".format(counter))
        return redirect ('/')
    else:
        return render_template ('info.html', name=request.form['name'], location=request.form['location'],language=request.form['language'],comment=request.form['comment'])

app.run(debug=True)   