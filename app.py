from flask import Flask, render_template, redirect, request, session, g, flash
import requests
from sqlalchemy.exc import IntegrityError
from flask_debugtoolbar import DebugToolbarExtension

# from forms import 
import helpers
from models import db, connect_db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer
from forms import AddUserForm, AddNotePlayer, AddNoteTeam
from helpers import get_player_by_id

CURR_USER_KEY = "curr_user"
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ball-dont-lie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

app.config['SECRET_KEY'] = 'I have a secret'

debug = DebugToolbarExtension(app)

# User signup/login/logout
@app.before_request
def add_user_to_g():
    """Check if logged in; add curr user to Flask global variable"""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None

def do_login(user):
    """Login user"""
    session[CURR_USER_KEY] = user.id

def do_logout():
    """Logout user"""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@app.route('/signup', methods=['GET','POST'])
def signup():
    """Handle user signup"""
    form = AddUserForm()
    if form.validate_on_submit():
        try:
            user = User.signup(
                username = form.username.data,
                email = form.email.data,
                password = form.password.data
            )
            import pdb
            pdb.set_trace()
            db.session.commit()
        except IntegrityError:
            flash("Username already taken", "danger")
            return render_template('users/signup.html', form=form)
        do_login(user)
        return redirect('/')
    else:
        return render_template("signup.html", form=form)

@app.route('/', methods=['GET','POST'])
def homepage():
    player_ids = [237, 117, 448]
    player_data = [get_player_by_id(id) for id in player_ids]
    return render_template('index.html', player_data=player_data)