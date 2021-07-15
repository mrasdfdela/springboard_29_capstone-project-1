from flask import Flask, render_template, redirect, request, session, g, flash, jsonify
import requests
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from flask_debugtoolbar import DebugToolbarExtension
from wtforms.fields.simple import PasswordField

# from forms import 
from models import db, connect_db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer
from forms import AddUserForm, LoginForm, AddNotePlayer, AddNoteTeam
from helpers import get_player_by_id, get_team_by_id,get_game_by_id, get_user_favteam_ids, get_user_favplayer_ids,  get_recent_games_by_days, convert_games_date_format, convert_player_gm_dt_fmt, get_seas_avgs, get_game_stats, get_player_stats_seas

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
            return render_template('user/signup.html', form=form)
        do_login(user)
        return redirect('/')
    else:
        return render_template("user/signup.html", form=form)

@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      user = User.authenticate(
          form.username.data,
          form.password.data
      )
      if user:
          do_login(user)
          flash(f"Hello, {user.username}!", "success")
          return redirect('/')
      else:
          flash("Invalid credentials", "danger")
  return render_template('user/login.html', form=form)

@app.route('/logout',methods=['GET','POST'])
def logout():
  """Log user out of the system."""
  if CURR_USER_KEY in session:
      del session[CURR_USER_KEY]
      flash ("Logged out.", "danger")
  return redirect('/')

@app.route('/user', methods=["GET", "POST"])
def profile():
    """Update profile for current user."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/login")

    form = AddUserForm(obj=g.user)
    if form.validate_on_submit():
        try: 
            user = User.authenticate(form.username.data, form.password.data)
            user.username=form.username.data
            user.email=form.email.data
            db.session.commit()
            flash("Edit recorded!", "success")
            return redirect(f'/user')
        except:
            flash("Invalid password/input","danger")
            return redirect('/user')

    return render_template("/user/edit.html", form=form)

# Show routes
@app.route('/', methods=['GET','POST'])
def homepage():
    recent_games = get_recent_games_by_days(7)
    games = convert_games_date_format(recent_games)
    return render_template('index.html', games=games)

@app.route('/user/<int:user_id>')
def show_user(user_id):
    if user_id == g.user.id:
        team_ids = get_user_favteam_ids(user_id)
        teams = [ get_team_by_id(id) for id in team_ids]

        player_ids = get_user_favplayer_ids(user_id)
        players = [ get_player_by_id(id) for id in player_ids]
        return render_template('user/user.html', user=g.user, players=players, teams=teams)
    else:
        return redirect(f"/user/{g.user.id}")

@app.route('/player/<int:player_id>',methods=['GET','POST'])
def show_player(player_id):
    """Show player profile"""

    try:
        player_note = NotePlayer.query.filter_by(user_id=g.user.id, player_id=player_id)
        form = AddNotePlayer(obj=player_note.all()[0])
    except:
        form = AddNotePlayer()

    if form.validate_on_submit():
        player_note.delete()
        note = NotePlayer(
            user_id=g.user.id,
            player_id=player_id,
            note=form.note.data)
        db.session.add(note)
        db.session.commit()
        flash("Note added!","success")
        return redirect(f"/player/{player_id}")
    else:
        try:
            fav_player_ids = [ p.player_id for p in g.user.favplayers ]
        except:
            fav_player_ids = False
        player = get_player_by_id(player_id)
        seas_stats = get_player_stats_seas(player_id)
        latest_games = convert_player_gm_dt_fmt(seas_stats[:5])

        season_avg = get_seas_avgs(player_id)

        if player:
            return render_template(
              'player.html', 
              user = g.user,
              player_ids = fav_player_ids,
              player = player, 
              season_avg = season_avg,
              latest_games = latest_games,
              form=form)
        else:
            return redirect("/")

@app.route('/team/<int:team_id>', methods=['GET','POST'])
def show_team(team_id):
    """Show team profile"""
    try:
        team_note = NoteTeam.query.filter_by(user_id=g.user.id, team_id=team_id)
        form = AddNoteTeam(obj=team_note.all()[0])
    except:
        form = AddNoteTeam()

    if form.validate_on_submit():
        team_note.delete()
        note = NoteTeam(
            user_id=g.user.id,
            team_id=team_id,
            note=form.note.data)
        db.session.add(note)
        db.session.commit()
        flash("Note added!","success")
        return redirect(f"/team/{team_id}")
    else:
        team = get_team_by_id(team_id)
        try:
            fav_team_ids = [ team.team_id for team in g.user.favteams ]
        except:
            fav_team_ids = False

        recent_games = get_recent_games_by_days(20,team_id)
        games = convert_games_date_format(recent_games)
        if team:
            return render_template("team.html", team=team, team_ids=fav_team_ids, games=games, form=form)
        else:
            return redirect("/")

@app.route('/game/<int:game_id>')
def show_game(game_id):
    """Show game details"""
    game = get_game_by_id(game_id)
    game = convert_games_date_format([game])[0]
    game_stats = get_game_stats(game_id)
    if game:
        return render_template(
          "game.html",
          game=game,
          game_stats=game_stats)
    else:
        return redirect("/")

# Like / Unlike routes
@app.route('/user/<int:user_id>/fav_player', methods=['POST','DELETE'])
def fav_player(user_id):
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