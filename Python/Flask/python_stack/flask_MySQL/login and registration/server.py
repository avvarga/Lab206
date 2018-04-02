from flask import Flask, request, render_template, redirect, flash, session
from mysqlconnection import MySQLConnector
import md5, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask (__name__)
mysql = MySQLConnector (app, 'login_registration')
app.secret_key='secret'

@app.route('/')
def index():
    query = "SELECT * FROM logins"
    logins = mysql.query_db(query)
    return render_template ('index.html', login_registration=logins)

@app.route('/register', methods=['POST'])
def register():
    registration=True
    pwd=False
    if len(request.form['email']) == 0 or len(request.form['first_name']) == 0 or len(request.form['last_name']) == 0 or len(request.form['password']) == 0 or len(request.form['pwd_confirm']) == 0:
        flash('All fields are required and must not be blank!')
        registration=False
    for letter in request.form['first_name'] or request.form['last_name']:
        if letter.isdigit():
            flash('First and Last Name cannot contain any numbers') 
            registration=False
            break
    if len(request.form['password'])<8:
        flash('Password must be at least 8 characters long.')
        registration=False
    if not pwd:
        flash('Password must contain at least 1 Uppercase letter and 1 number')
    for letter in request.form['password']:
        if letter.isdigit() and letter.isupper():
            pwd=True
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address.')
        registration=False
    if request.form['password']!=request.form['pwd_confirm']:
        flash('Password confirmation does not match the password entered')
        registration=False
    if registration:
        print 'Im here'
        query= "SELECT email FROM logins WHERE email= :email"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': md5.new(request.form['password']).hexdigest()
        }
        if mysql.query_db(query,data) == []:
            mysql.query_db("INSERT INTO logins (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())",data)
            return render_template('success.html')
    else:
        flash('This email is already registered')
        return redirect ('/')

@app.route('/login', methods=['POST'])
def login():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    user_query = "SELECT * FROM logins where logins.email = :email AND logins.password = :password"
    query_data = { 'email': email, 'password': password}
    user = mysql.query_db(user_query, query_data)
    return render_template('success.html')
app.run(debug=True)