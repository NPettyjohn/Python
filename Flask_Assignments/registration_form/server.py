# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['first_name']) < 1:
        flash("First name cannot be blank!")
    elif len(request.form['last_name']) < 1:
        flash("Last name cannot be blank!")
    elif len(request.form['password']) < 1:
        flash("Password cannot be blank!")
    elif len(request.form['password']) < 9:
        flash("Password must be at least 9 characters!")
    elif len(request.form['confirm_password']) < 1:
        flash("Confirm password cannot be blank!")
    elif request.form['confirm_password'] != request.form['password']:
        flash("The passwords you entered didn't match one another!")
    else:
        flash("Thanks for submitting your information. You are now signed up!")
    return redirect('/')

app.run(debug=True)
