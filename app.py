from flask import Flask, render_template, request
from login import *

role = None

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
            role = get_role()
            return render_template('user_added.html')
        else:
            return render_template('add.html')
    elif request.method == 'GET':
        return render_template('add.html')

@app.route("/charge", methods=['GET', 'POST'])
def charge():
    role = get_role()
    if role == "owner" or role == "employee":
        return render_template('charge.html')
    else:
        return render_template('no_access.html')

@app.route("/order", methods=['GET', 'POST'])
def order():
    role = get_role()
    if role == "owner":
        return render_template('order.html')
    else:
        return render_template('no_access.html')

@app.route("/schedule", methods=['GET', 'POST'])
def schedule():
    role = get_role()
    if role == "owner" or role == "employee" or role == "customer":
        return render_template('schedule.html')
    else:
        return render_template('no_access.html')

@app.route("/time", methods=['GET', 'POST'])
def add_time():
    role = get_role()
    if role == "owner" or role == "employee":
        return render_template('time.html')
    else:
        return render_template('no_access.html')  

@app.route("/login", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        submitted_pass = request.form['password']
        submitted_username = request.form['username']

        print("app.py")

        success = verify(submitted_username, submitted_pass)
        print(success)

        if success:
            role = get_role()
            return render_template('success.html')
        else:
            return render_template('nope.html')
    elif request.method == 'GET':
        return render_template('home.html')