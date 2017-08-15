from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def no_ninjas():
    return render_template("index.html")

@app.route('/ninja')
def show_all_ninjas():
    ninja_color='all'
    return render_template("ninjas_with_adv_routing.html", ninja_color=ninja_color)

@app.route('/ninja/<ninja_color>')
def show_user_profile(ninja_color):
    return render_template("ninjas_with_adv_routing.html", ninja_color=ninja_color)

app.run(debug=True)
