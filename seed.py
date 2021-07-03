from app import db
from models import User, FavTeam, FavPlayer, NoteTeam, NotePlayer

db.drop_all()
db.create_all()

db.session.commit()