from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'emailvalidation')

@app.route('/')
def index():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template ('index.html', emailvalidation=emails)

@app.route('/add', methods=['POST'])
def add():
    query= "SELECT email FROM emails WHERE email= :email"
    data = {
        'email': request.form['email']
    }
    if mysql.query_db(query,data) == []:
        mysql.query_db ("INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())",data)
        emails = mysql.query_db("SELECT * FROM emails")
        return render_template('success.html', emailvalidation = emails, email=request.form['email'] )
    else:
        flash ('Email is not Valid!')
        return redirect('/')
        

app.run(debug=True)