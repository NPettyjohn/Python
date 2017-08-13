from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/add_two')
def add_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    # session['counter'] = 1
    del session['counter']
    return redirect('/')

app.run(debug=True) # run our server
