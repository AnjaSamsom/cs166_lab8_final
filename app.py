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
        verified = verify(submitted_username, submitted_pass)
        print(verified)
        if verified:
            logged_in()
        else:
            not_logged_in()
    elif request.method == 'GET':
        return render_template('home.html')