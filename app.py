from flask import Flask, render_template, request
import requests, controllers
from flask_debugtoolbar import DebugToolbarExtension

# from forms import 
import helpers
from models import db, connect_db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer
# from controllers import c_homepage
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

@app.route('/', methods=['GET','POST'])
def homepage():
    player_ids = [237, 117, 448]
    player_data = [get_player_by_id(id) for id in player_ids]
    return render_template('index.html', player_data=player_data)