import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'num_to_guess' not in session:
        session['num_to_guess'] = random.randrange(0, 101)
        print session['num_to_guess']
    return render_template("index.html", num_to_guess=session['num_to_guess'])

@app.route('/check_guess', methods=['POST'])
def check_guess():
    user_guess = int(request.form['guess'])

    guess_type = type(user_guess)
    correct_number_type = type(session['num_to_guess'])

    if user_guess < session['num_to_guess']:
        guess_is_correct = False
        guess_feedback = "Too low!"
    elif user_guess > session['num_to_guess']:
        guess_is_correct = False
        guess_feedback = "Too high!"
    else:
        guess_is_correct = True
        guess_feedback = str(session['num_to_guess']) + " was the number!"

    return render_template("index.html", guess_feedback=guess_feedback, guess_is_correct=guess_is_correct, guess=user_guess, num_to_guess=session['num_to_guess'])

@app.route('/play_again')
def play_again():
    session.pop('num_to_guess')
    return redirect('/')



# @app.route('/add_two')
# def add_two():
#     session['counter'] += 1
#     return redirect('/')
#
# @app.route('/reset')
# def reset():
#     # session['counter'] = 1
#     del session['counter']
#     return redirect('/')

app.run(debug=True) # run our server
