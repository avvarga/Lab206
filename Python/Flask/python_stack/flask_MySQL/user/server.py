from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends')

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    query = "SELECT *, CONCAT(first_name, ' ',last_name) AS name FROM friends"                           
    friends = mysql.query_db(query)                          
    return render_template('index.html',full_friends=friends) 

@app.route('/users/create', methods = ['POST'])
def add():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query,data)
    return redirect('/users')

@app.route('/users/<id>', methods = ['POST', 'GET'])
def show(id):
    if request.method == 'GET':
        query = "SELECT *, CONCAT(first_name,' ',last_name) AS full_name FROM friends WHERE id=:id"
        data = {
            'id': id
        }
        user = mysql.query_db(query, data)
        return render_template('show.html',user=user)
    else:
        query = " UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': id
        }
        mysql.query_db(query,data)
        return redirect ('/')

@app.route('/users/<id>/edit')
def edit(id):
    return render_template('edit.html', id=id)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/<id>/destroy')
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        'id': id
    }
    mysql.query_db(query,data)
    return redirect ('/')

app.run(debug=True)