from flask import Flask, render_template, session, redirect, request
import random
import math

app = Flask(__name__)
app.secret_key = 'somekey'

@app.route('/')
def home():

    session['message'] = 'Activity'

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def winnings():

    if request.form['building'] == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold
        session['feed'] = 'You went to the farm and received %d gold!' %gold

    if request.form['building'] == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
        session['feed'] = 'You went to the cave and received %d gold!' %gold

    if request.form['building'] == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
        session['feed'] = 'You went to the house and received %d gold!' %gold

    if request.form['building'] == 'casino':
        gold = random.randint(-50,50)
        session['gold'] += gold
        if gold<0:
            session['feed']= 'You went to the casino and lost %d gold!' %gold
        else:
            session['feed'] = 'You went to the casino and received %d gold!' %gold


    return redirect ('/')


app.run(debug=True)
