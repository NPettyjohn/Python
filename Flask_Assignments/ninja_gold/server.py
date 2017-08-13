import random, time
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['gold_count'] = 0
    session['log'] = []
    return render_template("index.html", session_log=session['log'], gold_count=session['gold_count'])


@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building=="farm":
        gold_change = random.randrange(10, 21)
        session['gold_count'] += gold_change
        localtime = time.asctime( time.localtime(time.time()) )
        session['log'].append((True, "Earned " + str(gold_change) + " golds from the farm! (" + str(localtime) + ")"))
        session.modified = True
    elif building=="cave":
        gold_change = random.randrange(5, 11)
        session['gold_count'] += gold_change
        localtime = time.asctime( time.localtime(time.time()) )
        session['log'].append((True, "Earned " + str(gold_change) + " golds from the cave! (" + str(localtime) + ")"))
        session.modified = True
    elif building=="house":
        gold_change = random.randrange(2, 6)
        session['gold_count'] += gold_change
        localtime = time.asctime( time.localtime(time.time()) )
        session['log'].append((True, "Earned " + str(gold_change) + " golds from the house! (" + str(localtime) + ")"))
        session.modified = True
    elif building=="casino":
        gold_change = random.randrange(-50, 51)
        session['gold_count'] += gold_change
        localtime = time.asctime( time.localtime(time.time()) )
        if gold_change >= 0:
            session['log'].append((True, "Earned " + str(gold_change) + " golds from the casino! (" + str(localtime) + ")"))
            session.modified = True
        else:
            session['log'].append((False, "Entered a casino and lost " + str(abs(gold_change)) + " golds... ouch. (" + str(localtime) + ")"))
            session.modified = True
    return render_template("index.html", building=building, session_log=session['log'], gold_count=session['gold_count'])

app.run(debug=True)
