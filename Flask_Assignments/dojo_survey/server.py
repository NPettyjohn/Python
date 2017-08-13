from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def display_results():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Comment cannot be empty!")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comment cannot be longer than 120 characters!")
        return redirect('/')
    else:
        # flash("Success! Your name is {}".format(request.form['name']))
        name = request.form['name']
        location = request.form['location']
        language = request.form['favorite_language']
        comment = request.form['comment']
        return render_template("result.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True) # run our server
