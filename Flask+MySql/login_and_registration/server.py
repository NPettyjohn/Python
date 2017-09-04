from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\.\+_-]*$')
app = Flask(__name__)
app.secret_key = "SuperSecretKey"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_and_registration_db')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['first_name']) < 2:
        flash("First name must be at least two characters long.")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("First name must only contain letters.")
        return redirect('/')
    elif len(request.form['last_name']) < 2:
        flash("Last name must be at least two characters long.")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Last name must only contain letters.")
        return redirect('/')
    elif len(request.form['email_address']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash("Email address must be in a valid format. For instance: 'mike@mike.com' ")
        return redirect('/')
    elif len(request.form['password']) < 7:
        flash("Password must be at least eight characters.")
        return redirect('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash("The passwords you entered did not match.")
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email_address, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email_address, :pw_hash, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email_address': request.form['email_address'],
            'pw_hash': bcrypt.generate_password_hash(request.form['password'])
           }
        mysql.query_db(query, data)
        session['user'] = request.form['email_address']
        return render_template('success.html')

@app.route('/login', methods=['GET'])
def render_login():
    return render_template('login.html')

@app.route('/login_user', methods=['POST'])
def login():
    email_address = request.form['email_address']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email_address = :email_address LIMIT 1"
    query_data = { 'email_address': email_address }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        # login user
        session['user'] = request.form['email_address']
        return render_template('success.html')
    else:
        # set flash error message and redirect to login page
        flash("Could not log you in with the email address and password you provided. Please try again.")
        return redirect('/login')


app.run(debug=True)
