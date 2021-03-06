from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    """User model"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    favplayers = db.relationship('FavPlayer', backref='users')
    favteams = db.relationship('FavTeam', backref='users')
    notesplayers = db.relationship('NotePlayer', backref='users')
    notesteams = db.relationship('NoteTeam', backref='users')

    @classmethod
    def signup(cls, username, email, password):
        """Sign up user using hashed password"""
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(
          username = username,
          email=email,
          password=hashed_pwd
        )
        db.session.add(user)
        return user
    @classmethod
    def authenticate(cls, username, password):
        """Authentication for login"""
        user = cls.query.filter_by(username=username).first()
        if user:
            # import pdb
            # pdb.set_trace()
            is_auth = bcrypt.check_password_hash(user.password, password.encode())
            if is_auth:
                return user
        return False


class FavTeam(db.Model):
    """Users' favorite teams"""

    __tablename__ = 'fav_teams'

    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.id'),
        nullable=False, 
        primary_key=True)
    team_id = db.Column(
        db.Integer, 
        nullable=False, 
        primary_key=True)

class FavPlayer(db.Model):
    """Users' favorite players"""

    __tablename__ = 'fav_players'

    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.id'),
        nullable=False, 
        primary_key=True)
    player_id = db.Column(
        db.Integer, 
        nullable=False, 
        primary_key=True)

class NoteTeam(db.Model):
    """User notes about teams"""

    __tablename__ = 'team_notes'

    id = db.Column(
        db.Integer, 
        primary_key=True)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.id'),
        nullable=False)
    team_id = db.Column(
        db.Integer, 
        nullable=False)
    note = db.Column(
        db.Text, 
        nullable=False)

class NotePlayer(db.Model):
    """Player notes about teams"""

    __tablename__ = 'player_notes'

    id = db.Column(
        db.Integer, 
        primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False)
    player_id = db.Column(
        db.Integer, 
        nullable=False)
    note = db.Column(
        db.Text, 
        nullable=False)

def connect_db(app):
    """Connect this database to provide Flask app. To be called in the Flask app"""

    db.app = app
    db.init_app(app)