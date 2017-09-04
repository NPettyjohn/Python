from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "SuperSecretKey"
mysql = MySQLConnector(app,'full_friends_db')
@app.route('/', methods=['GET'])
def index():
    query = "SELECT * FROM friends"
    friends_recordset = mysql.query_db(query)
    return render_template('index.html', friends_recordset=friends_recordset)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email_address, created_at, updated_at) VALUES (:first_name, :last_name, :email_address, NOW(), NOW())"
    data = {
         'first_name': request.form['first_name'],
         'last_name': request.form['last_name'],
         'email_address': request.form['email_address'],
       }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    #Renders the template for editing a friend.
    query = "SELECT * FROM friends WHERE id=" + str(id)
    friends_recordset = mysql.query_db(query)
    record_to_edit = friends_recordset[0]
    return render_template('edit_friend.html', record_to_edit=record_to_edit, id=id)


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    #Updates record in the database.
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email_address=:email_address, updated_at=NOW() WHERE id=" + str(id)
    data = {
         'first_name': request.form['first_name'],
         'last_name': request.form['last_name'],
         'email_address': request.form['email_address'],
       }
    mysql.query_db(query, data)
    flash("Successfully updated friend!")
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id=" + str(id)
    mysql.query_db(query)
    flash("Successfully deleted friend!")
    return redirect('/')


# ##############################################################
# @app.route('/validate', methods=['POST'])
# def validate():
#     if len(request.form['email']) < 1:
#         flash("Email cannot be blank!")
#         return redirect('/')
#     elif not EMAIL_REGEX.match(request.form['email']):
#         flash("Email is not valid!")
#         return redirect('/')
#     else:
#         query = "INSERT INTO email_addresses (address, created_at, updated_at) VALUES (:address, NOW(), NOW())"
#         data = {
#              'address': request.form['email'],
#            }
#         mysql.query_db(query, data)
#
#         query = "SELECT id, address, created_at FROM email_addresses"
#         email_recordset = mysql.query_db(query)
#
#         return render_template('success.html',entered_email=request.form['email'], email_recordset=email_recordset)
#
# @app.route('/delete/<id>', methods=['GET'])
# def delete_record(id):
#         query = "DELETE FROM email_addresses WHERE id=" + str(id)
#         email_recordset = mysql.query_db(query)
#
#         query = "SELECT id, address, created_at FROM email_addresses"
#         email_recordset = mysql.query_db(query)
#         return render_template('success.html', email_recordset=email_recordset)

app.run(debug=True)
