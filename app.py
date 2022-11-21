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

@app.route("/user_added", methods=['GET', 'POST'])
def user_added():
    return render_template('user_added.html')


@app.route("/new_user", methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        password = request.form['password']
        username = request.form['username']
        # this method returns the true if the password is valid
        # and false if not, so we will send them to another
        # page if the password isn't valid
        success = add_user(username, password)
        print(success)
        if success:
            return render_template('user_added.html')
        else:
            return render_template('add.html')
    elif request.method == 'GET':
        return render_template('add.html')

@app.route("/charge", methods=['GET', 'POST'])
def charge():
    return render_template('charge.html')

@app.route("/order", methods=['GET', 'POST'])
def order():
    return render_template('order.html')

@app.route("/schedule", methods=['GET', 'POST'])
def schedule():
    return render_template('schedule.html')

@app.route("/time", methods=['GET', 'POST'])
def add_time():
    return render_template('time.html')
    
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