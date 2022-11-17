from flask import Flask, render_template, request

app = Flask(__name__)

# run this with flask --app app run
@app.route("/", methods=['GET', 'POST'])
def home():
    # Home page
    return render_template('home.html')



