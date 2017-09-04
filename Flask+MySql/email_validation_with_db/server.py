from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "SuperSecretKey"
mysql = MySQLConnector(app,'email_validation_assignment')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    else:
        query = "INSERT INTO email_addresses (address, created_at, updated_at) VALUES (:address, NOW(), NOW())"
        data = {
             'address': request.form['email'],
           }
        mysql.query_db(query, data)

        query = "SELECT id, address, created_at FROM email_addresses"
        email_recordset = mysql.query_db(query)

        return render_template('success.html',entered_email=request.form['email'], email_recordset=email_recordset)

@app.route('/delete/<id>', methods=['GET'])
def delete_record(id):
        query = "DELETE FROM email_addresses WHERE id=" + str(id)
        email_recordset = mysql.query_db(query)

        query = "SELECT id, address, created_at FROM email_addresses"
        email_recordset = mysql.query_db(query)
        return render_template('success.html', email_recordset=email_recordset)

app.run(debug=True)
