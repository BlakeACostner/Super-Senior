# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask, render_template  # Flask is the web app that we will customize


app = Flask(__name__)     # creates the app

#HOME PAGE
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#LIST NOTES PAGE
@app.route('/notes')
def get_notes():
    notes= {1: {'title': 'First note', 'text': 'this is my first note', 'date': '10-1-2020'}}

    return render_template('notes.html', notes = notes)

#SPECIFIC NOTE PAGE
@app.route('/notes/<note_id>')
def get_note(note_id):
    notes= {1: {'title': 'First note', 'text': 'this is my first note', 'date': '10-1-2020'}}
    
    return render_template('note.html', notes = notes[int(note_id)])






app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)
