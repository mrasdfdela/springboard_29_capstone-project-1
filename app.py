from flask import Flask, render_template, redirect, request, session, g, flash, jsonify
import requests
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from flask_debugtoolbar import DebugToolbarExtension

# from forms import 
import helpers
from models import db, connect_db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer
from forms import AddUserForm, AddNotePlayer, AddNoteTeam
from helpers import get_player_by_id, get_user_favteam_ids, get_user_favplayer_ids, get_team_by_id, get_recent_games, convert_gameday_format

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

@app.route('/user/<int:user_id>')
def show_user(user_id):
    if user_id == g.user.id:
        return render_template('user.html',user=g.user)
    else:
        return redirect(f"/user/{g.user.id}")

@app.route('/player/<int:player_id>')
def show_player(player_id):
    player = get_player_by_id(player_id)
    fav_player_ids = [ player.player_id for player in g.user.favplayers ]
    if player:
        return render_template('player.html', player=player, player_ids = fav_player_ids)
    else:
        return redirect("/")

@app.route('/team/<int:team_id>')
def show_team(team_id):
    """Show team profile"""
    team = get_team_by_id(team_id)
    fav_team_ids = [ team.team_id for team in g.user.favteams ]
    if team:
        return render_template("team.html", team=team, team_ids=fav_team_ids)
    else:
        return redirect("/")

# Like / Unlike routes
@app.route('/user/<int:user_id>/fav_player', methods=['POST','DELETE'])
def fav_player(user_id):
    # pdb.set_trace()
    if request.method == 'POST' and user_id == g.user.id:
        try:
            fav_player = FavPlayer(
              user_id = user_id,
              player_id = request.json['params']['player_id']
            )
            db.session.add(fav_player)
            db.session.commit()

            player_ids = get_user_favplayer_ids(user_id)
            return jsonify(player_ids),201
        except:
            return redirect(f'/user/{g.user.id}')
    elif request.method == 'DELETE' and user_id == g.user.id:
        try:
            FavPlayer.query.filter_by(user_id=user_id, player_id=request.args['player_id']).delete()
            db.session.commit()

            player_ids = get_user_favplayer_ids(user_id)
            return jsonify(player_ids),201
        except:
            return redirect(f'/user/{g.user.id}')
    else:
        return redirect('/')

@app.route('/user/<int:user_id>/fav_team', methods=['POST','DELETE'])
def fav_team(user_id):
    if request.method == 'POST' and user_id == g.user.id:
        try:
            fav_team = FavTeam(
              user_id = user_id,
              team_id = request.json['params']['team_id']
            )
            db.session.add(fav_team)
            db.session.commit()

            team_ids = get_user_favteam_ids(user_id)
            return jsonify(team_ids),201
        except:
            return redirect(f'/user/{g.user.id}')
    elif request.method == 'DELETE' and user_id == g.user.id:
        try:
            FavTeam.query.filter_by(user_id=user_id, team_id=request.args['team_id']).delete()
            db.session.commit()

            team_ids = get_user_favteam_ids(user_id)
            return jsonify(team_ids),201
        except:
            return redirect(f'/user/{g.user.id}')
    else:
        return redirect('/')