# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask, render_template  # Flask is the web app that we will customize


app = Flask(__name__)     # creates the app


@app.route('/index')
def index():
    return render_template('index.html')


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)
