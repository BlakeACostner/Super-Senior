# imports
import os # os is used to get environment variables IP & PORT

from flask import Flask, render_template, request, redirect, url_for, session # Flask is the web app that we will customize
from forms import RegisterForm, LoginForm, CommentForm
from flask_bcrypt import Bcrypt
from database import db
from models import Note as Note 
from models import User as User
from models import Comment as Comment




 # creates the app
app = Flask(__name__)    


# sets the encryption 
bcrypt = Bcrypt(app)
app.secret_key = "super secret key"
app.config['SECRETY_KEY'] = 'SE3155'


# sets the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)


# Setup models for database  
with app.app_context():
    db.create_all()   


# Homepage route
@app.route('/')
@app.route('/index')
def index():
    if session.get('user'):
        # gets user's session if they have an account 
      return render_template('index.html', user = session['user'])
    return render_template("index.html")



# Notes route
@app.route('/notes')
def get_notes():
    if session.get('user'):
        # gets notes from user's database 
        my_notes = db.session.query(Note).filter_by(user_id=session['user_id']).all()

        return render_template('notes.html', notes=my_notes, user=session['user'])
    else:
        return redirect(url_for('login'))



# Specific note route 
@app.route('/notes/<note_id>')
def get_note(note_id):
    
    if session.get('user'):
        # gets note from database and renders it 
        my_note = db.session.query(Note).filter_by(id=note_id, user_id=session['user_id']).one()
        form = CommentForm()
        return render_template('note.html', note = my_note, user =session['user'], form=form)
    else:
        return redirect(url_for('login'))



# New note route
@app.route('/notes/new', methods=['GET','POST'])
def new_note():
    if session.get('user'):
        #check method 
        if request.method == 'POST':
            # gets note objects 
            title = request.form['title']
            text = request.form['noteText']
            members = request.form['noteMembers']
            # create time stamp
            from datetime import date 
            today = date.today()
            # format date 
            today = today.strftime("%m-%d-%Y")
            new_record = Note(title,text, members, today, session['user_id'])
            db.session.add(new_record)
            db.session.commit()

            return redirect(url_for('get_notes'))
        else:
            return render_template('new.html', user = session['user'])
    else:
        return redirect(url_for('login'))



# Edited note route
@app.route('/notes/edit/<note_id>', methods=['GET', 'POST'])
def update_note(note_id):
    
    if session.get('user'):
        if request.method == 'POST':

            # gets note objects 
            title = request.form['title']
            text = request.form['noteText']
            members = request.form['noteMembers']

            note = db.session.query(Note).filter_by(id=note_id).one()
            note.title = title
            note.text = text
            note.members = members

            # commits 
            db.session.add(note)
            db.session.commit()

            return redirect(url_for('get_notes'))
        else:
            my_note = db.session.query(Note).filter_by(id=note_id).one()
            return render_template('new.html', note=my_note, user=session['user'])
    else: 
        return redirect(url_for('login'))



# Route for deleting note 
@app.route('/notes/delete/<note_id>', methods=['POST'])
def delete_note(note_id):
    if session.get('user'):
        my_note = db.session.query(Note).filter_by(id=note_id).one()
        db.session.delete(my_note)
        db.session.commit()

        return redirect(url_for('get_notes'))
    else:
        return redirect(url_for('login'))



# Route for posting a comment to a task 
@app.route('/notes/<note_id>/comment', methods=['POST'])
def new_comment(note_id):
    if session.get('user'):
        comment_form = CommentForm()
        # validate_on_submit only validates using POST
        if comment_form.validate_on_submit():
            # get comment data
            comment_text = request.form['comment']
            new_record = Comment(comment_text, int(note_id), session['user_id'])
            db.session.add(new_record)
            db.session.commit()

        return redirect(url_for('get_note', note_id=note_id))
    else:
        return redirect(url_for('login'))



# Route for registering an account 
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        # generates password hash
        h_password = bcrypt.generate_password_hash(request.form['password'])
        
        # get entered user data
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        # create new user
        new_user = User(first_name, last_name, request.form['email'], h_password)
        # add user to database and commit
        db.session.add(new_user)
        db.session.commit()
        # save the user's name to the session
        session['user'] = first_name
        session['user_id'] = new_user.id  
        # show user dashboard view
        return redirect(url_for('get_notes'))

    # error register view 
    return render_template('register.html', form=form)



# Route for login
@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # validate_on_submit only validates using POST
    if login_form.validate_on_submit():

        the_user = db.session.query(User).filter_by(email=request.form['email']).one()

        if bcrypt.check_password_hash( the_user.password, request.form['password']):
            # password match and adding user info to the session
            session['user'] = the_user.first_name
            session['user_id'] = the_user.id
            # render note view
            return redirect(url_for('get_notes'))

        # password check failed
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login.html", form=login_form)



# Route for logging out 
@app.route('/logout')
def logout():
    # check if a user is saved in session
    if session.get('user'):
        session.clear()
    # returns the hompage "index" after logging out    
    return redirect(url_for('index'))



app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)