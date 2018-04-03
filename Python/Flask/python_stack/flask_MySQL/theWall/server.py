from flask import Flask, request, render_template, redirect, flash, session
from mysqlconnection import MySQLConnector
import md5, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask (__name__)
mysql = MySQLConnector (app, 'theWall')
app.secret_key='secret'

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template ('index.html', theWall=users)

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
        query= "SELECT email FROM users WHERE email= :email"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': md5.new(request.form['password']).hexdigest()
        }
        if mysql.query_db(query,data) == []:
            mysql.query_db("INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())",data)
            query2 = "SELECT * FROM users WHERE users.email= :email"
            user = mysql.query_db (query2,data)
            session ['user'] = user[0]
            return redirect('/wall')
            
    else:
        flash('This email is already registered')
        return redirect ('/')

@app.route('/login', methods=['POST'])
def login():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
    query_data = { 'email': email, 'password': password}
    user = mysql.query_db(user_query, query_data)
    if user != []:
        session['user'] = user[0]
        return render_template('wall.html')
    else:
        flash ('Incorrect user information')
        return redirect ('/')


@app.route('/logoff')
def logoff():
    session.clear()
    return redirect('/')

@app.route('/post_message', methods = ['POST'])
def post_message():
    if len(request.form['message'])>0:
        print session['user']
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
        data = {
            'user_id': session['user']['id'],
            'message': request.form['message']
        }
        mysql.query_db(query,data)
    return redirect ('/wall')

@app.route('/comment', methods = ['POST'])
def comment():
    if len(request.form['comment'])>0:
        print session['user']
        query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
        data = {
            'user_id': session['user']['id'],
            'message_id': request.form['message_id'],
            'comment': request.form['comment']
        }
        mysql.query_db(query,data)
    return redirect ('/wall')

@app.route('/wall')
def wall():
    session['messages']=mysql.query_db("SELECT *, messages.id AS messages_id FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC")
    session['comments']=mysql.query_db("SELECT * FROM comments JOIN users ON users.id = comments.user_id JOIN messages ON messages.id = comments.message_id ORDER BY comments.created_at DESC")
    return render_template ('wall.html')



app.run(debug=True)