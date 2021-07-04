from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class AddUserForm(FlaskForm):
    """Form for adding users"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[Email()])
    password = PasswordField('Password', validators=[Length(min=6)])

class AddNotePlayer(FlaskForm):
    """Form for adding user notes about Player"""
    note = TextAreaField("Player Note")

class AddNoteTeam(FlaskForm):
    """Form for adding user notes about Player"""
    note = TextAreaField("Team Note")