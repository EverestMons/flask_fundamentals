from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.php")


@app.route('/result',methods=["POST"])
def result():
    return render_template("result.html", name = request.form['name'] ,
    com = request.form['comment'] ,
    location = request.form['location'] ,
    favlang = request.form['favlang'])
    return redirect('/')
app.run(debug=True)
