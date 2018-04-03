from flask import Flask, render_template, request, redirect, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)                     
app.secret_key='secret'                   
                                 
@app.route('/')
def index():                                  
    return render_template ('index.html')  

@app.route('/register', methods=['POST'])
def register():
    registration=True
    pwd=False
    if len(request.form['email']) == 0 or len(request.form['first_name']) == 0 or len(request.form['last_name']) == 0 or len(request.form['password']) == 0 or len(request.form['confirmation']) == 0:
        flash('All fields are required and must not be blank!')
        registration=False
    for letter in request.form['first_name'] or request.form['last_name']:
        if letter.isdigit():
            flash('First and Last Name cannot contain any numbers') 
            registration=False
            break
    if len(request.form['password'])<9:
        flash('Password must be at least 9 characters long.')
        registration=False
    if not pwd:
        flash('Password must contain at least 1 Uppercase letter and 1 number')
    for letter in request.form['password']:
        if letter.isdigit() and letter.isupper():
            pwd=True
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address.')
        registration=False
    if request.form['password']!=request.form['confirmation']:
        flash('Password confirmation does not match the password entered')
        registration=False
    if registration and pwd:
        flash('Thanks for submitting your information!')
    return redirect ('/')
app.run(debug=True)   