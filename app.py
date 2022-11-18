from flask import Flask, render_template, request
from login import *

app = Flask(__name__)
conn = sqlite3.connect("login_info.db")
cur = conn.cursor()

# run this with flask --app app run


@app.route("/success", methods=['GET', 'POST'])
def logged_in():
    return render_template('success.html')

@app.route("/nope", methods=['GET', 'POST'])
def not_logged_in():
    return render_template('nope.html')

@app.route("/login", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        submitted_pass = request.form['password']
        submitted_username = request.form['username']
        success = verify(submitted_username, submitted_pass)
        print("working on it...")
        print(success)
        if success:
            return render_template('success.html')
        else:
            return render_template('nope.html')
    elif request.method == 'GET':
        return render_template('home.html')