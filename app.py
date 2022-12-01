from flask import Flask, render_template, request
from login import *

role = None
user = None
try_counter = 0


app = Flask(__name__)
conn = sqlite3.connect("login_info.db")
cur = conn.cursor()

# run this with flask --app app run

@app.route("/success", methods=['GET', 'POST'])
def logged_in():
    role = get_role()
    user = get_user()
    return render_template('success.html', username=user, role=role)

@app.route("/nope", methods=['GET', 'POST'])
def not_logged_in():
    return render_template('nope.html')

@app.route("/user_added", methods=['GET', 'POST'])
def user_added():
    return render_template('user_added.html')

@app.route("/new_user", methods=['GET', 'POST'])
def new_user():
    role = get_role()
    if role == "owner":
        if request.method == 'POST':
            password = request.form['password']
            username = request.form['username']

            # sanitizing input
            password = sanitize(password)
            username = sanitize(username)

            print(username)
            
            # this method returns the true if the password is valid
            # and false if not, so we will send them to another
            # page if the password isn't valid
            value = add_user(username, password)
            success = value[0]
            generated_password = value[1]
            error = "Please select a valid password and an unused username"
            print(success)
            if success:
                role = get_role()
                print(generated_password)
                return render_template('user_added.html', password=generated_password, username=username)
            else:
                return render_template('add.html', error=error)
        elif request.method == 'GET':
            return render_template('add.html', error = "")
    else:
        return render_template('no_access.html')

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

@app.route("/", methods=['GET', 'POST'])
def home():
    if try_counter >= 3:
        message = "You have tried and failed three times, please restart the application and remember your password"
        return render_template('nope.html', text=message)
    elif request.method == 'POST':
        submitted_pass = request.form['password']
        submitted_username = request.form['username']

        try_counter +=1

        # sanitizing input
        submitted_pass = sanitize(submitted_pass)
        submitted_username = sanitize(submitted_username)

        success = verify(submitted_username, submitted_pass)

        if success:
            role = get_role()
            user = submitted_username
            try_counter =0
            return render_template('success.html', username=submitted_username, role=role)
        else:
            try_counter += 1
            message = "Given username and password do not match, please enter the correct information"
            return render_template('nope.html', text=message)
    elif request.method == 'GET':
        return render_template('home.html')
