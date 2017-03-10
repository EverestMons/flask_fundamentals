from flask import Flask, render_template, session, request, redirect
import random
app = Flask (__name__)

app.secret_key = "secretkey"

@app.route('/')
def index ():
    if 'message' not in session:
        session['message'] = ""
    if 'submission' not in session:
        session ['submission']  = random.randrange(1,101)
    return render_template ('index.html')

@app.route('/checknum', methods = ['POST'])
def checknum ():
    num = int(request.form['submission'])
    if num == session['submission']:
        session['message'] = 'you win!'
    elif num > session['submission']:
        session['message'] = 'too high!'
    else:
        session['message'] = 'too low!'

        return redirect ('/')

@app.route('/reset')
def reset ():
    session.pop('submission')
    session.pop('message')
    return redirect('/')




app.run(debug=True)
