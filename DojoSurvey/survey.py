from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'thekey'
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process', methods=["POST"])
def process():
    if len(request.form["name"]) < 1:
        flash("Please give your name")
        return redirect('/')
    if len(request.form["comment"]) < 1:
        flash("Please make a comment")
        return redirect('/')
    if len(request.form["comment"]) > 120:
        flash("Comment must be under 120 characters")
        return redirect('/')
    else:
        flash("Success")
    return redirect('/')
app.run(debug=True)
