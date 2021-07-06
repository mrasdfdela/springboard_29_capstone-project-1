from flask import Flask, render_template, redirect, request, session, g, flash
import requests
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from flask_debugtoolbar import DebugToolbarExtension

# from forms import 
import helpers
from models import db, connect_db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer
from forms import AddUserForm, AddNotePlayer, AddNoteTeam
from helpers import get_player_by_id, get_team_by_id, get_recent_games, convert_gameday_format

import pdb

CURR_USER_KEY = "curr_user"
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ball-dont-lie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

app.config['SECRET_KEY'] = 'I have a secret'

# debug = DebugToolbarExtension(app)

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
            db.session.commit()
        except IntegrityError:
            flash("Username already taken", "danger")
            return render_template('users/signup.html', form=form)
        do_login(user)
        return redirect('/')
    else:
        return render_template("signup.html", form=form)



# Show routes
@app.route('/', methods=['GET','POST'])
def homepage():
    recent_games = get_recent_games(5)['data']
    games = convert_gameday_format(recent_games)
    return render_template('index.html', games=games)

@app.route('/team/<int:team_id>')
def show_team(team_id):
    """Show team profile"""
    team = get_team_by_id(team_id)
    if team:
        return render_template("team.html", team=team)
    else:
        return redirect("/")

@app.route('/player/<int:player_id>')
def show_player(player_id):
    player = get_player_by_id(player_id)
    if player:
        return render_template('player.html', player=player)
    else:
        return redirect("/")

@app.route('/user/<int:user_id>')
def show_user(user_id):
    if user_id == g.user.id:
        # pdb.set_trace()
        return render_template('user.html',user=g.user)
    else:
        return redirect(f"/user/{g.user.id}")