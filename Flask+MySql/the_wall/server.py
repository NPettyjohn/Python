from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\.\+_-]*$')
app = Flask(__name__)
app.secret_key = "SuperSecretKey"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall_db')
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
    elif len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email address must be in a valid format. For instance: 'mike@mike.com' ")
        return redirect('/')
    elif len(request.form['password']) < 7:
        flash("Password must be at least eight characters.")
        return redirect('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash("The passwords you entered did not match.")
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
           }
        mysql.query_db(query, data)
        session['user'] = request.form['email']
        return redirect('/wall')

@app.route('/login', methods=['GET'])
def render_login():
    return render_template('login.html')

@app.route('/login_user', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['password'], password):
        # login user
        session['user'] = request.form['email']
        return redirect('/wall')
    else:
        # set flash error message and redirect to login page
        flash("Could not log you in with the email address and password you provided. Please try again.")
        return redirect('/login')

@app.route('/wall', methods=['GET'])
def display_wall():
    if session['user'] != "":
        query = ("SELECT 	messages.id as message_id, messages.user_id as user_id, messages.message as message, messages.created_at as created_at, users.first_name as first_name, users.last_name as last_name, users.email as email FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC")
        messages_query = mysql.query_db(query)
        query = "SELECT	messages.id as message_id, comments.id as comment_id, comment as comment, users.first_name as first_name, users.last_name as last_name, comments.created_at as created_at FROM messages JOIN comments ON messages.id = comments.message_id JOIN users ON comments.user_id = users.id ORDER BY messages.id DESC, comments.id "
        comments_query = mysql.query_db(query)
        return render_template('wall.html', wall_messages=messages_query, wall_comments=comments_query)
    else:
        # User isn't logged in.
        return redirect('/')

@app.route('/message/post', methods=['POST'])
def post_message():
    email = session['user']
    print email
    query = "SELECT id FROM users where email = :email"
    data = {
        'email':email
        }
    user_id_query = mysql.query_db(query, data)
    user_id = user_id_query[0]['id']
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        'user_id': user_id,
        'message': request.form['message']
       }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/post/<message_id>', methods=['POST'])
def post_comment(message_id):
    email = session['user']
    print email
    query = "SELECT id FROM users where email = :email"
    data = {
        'email':email
        }
    user_id_query = mysql.query_db(query, data)
    user_id = user_id_query[0]['id']
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    data = {
        'user_id': user_id,
        'message_id': message_id,
        'comment': request.form['comment']
       }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/message/delete/<message_id>', methods=['GET'])
def delete_message(message_id):
    query = "DELETE FROM comments where message_id = :message_id"
    data = {
        'message_id': message_id
        }
    mysql.query_db(query, data)
    query = "DELETE FROM messages where id = :message_id"
    data = {
        'message_id': message_id
        }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/logoff', methods=['GET'])
def logoff():
    session['user'] = ""
    flash("You have successfully been logged out.")
    return redirect('/')

app.run(debug=True)
