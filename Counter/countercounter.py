from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/')

def index():
    session['count'] += 1
    return render_template('home.html')

@app.route('/ninja')

def button1():
    session['count'] += 2
    return render_template('home.html')

@app.route('/hacker')

def button2():
    session['count'] = 1
    return render_template('home.html')

app.run(debug=True)
