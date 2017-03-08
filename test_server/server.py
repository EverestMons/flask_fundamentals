from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def count():
  session["theRealCount"] += 1
  return render_template('user.html', p =session["theRealCount"])

app.run(debug=True)
