from app import db
from models import User, FavTeam, FavPlayer, NoteTeam, NotePlayer

db.drop_all()
db.create_all()

jerry = User.signup(
  username = "jerryhsu",
  email = "jerryhsu830@gmail.com",
  password = "verysecurepassword"
)
rachel = User.signup(
  username = "rachelliou",
  email = "rachel.liou@gmail.com",
  password = "supersecretpassword"
)
db.session.commit()

lebron = FavPlayer(
  user_id = rachel.id,
  player_id = 237
)

kyrie = FavPlayer(
  user_id = rachel.id,
  player_id = 228
)

durant = FavPlayer(
  user_id = jerry.id,
  player_id = 140
)

harden = FavPlayer(
  user_id = jerry.id,
  player_id = 192
)

cavs = FavTeam(
  user_id = rachel.id,
  team_id = 6
)

lakers = FavTeam(
  user_id = rachel.id,
  team_id = 14
)

okc = FavTeam(
  user_id = jerry.id,
  team_id = 21
)

bk = FavTeam(
  user_id = jerry.id,
  team_id = 3
)

db.session.add_all([lebron, kyrie, durant, harden, cavs, lakers, okc, bk])
db.session.commit()

lebron_note = NotePlayer(
  user_id = 1,
  player_id = 237,
  note = 'GOAT, baby, or baby goat?'
)

kyrie_note = NotePlayer(
  user_id = 2,
  player_id = 228,
  note = 'The world is flat'
)

brooklyn_note = NoteTeam(
  user_id = 1,
  team_id = 3,
  note = 'Former known as the New Jersey Nets.'
)

cavs_note = NoteTeam(
  user_id = 2,
  team_id = 6,
  note = "What's the difference between Miami and Cleveland? It's the same."
)

db.session.add_all([lebron_note,kyrie_note,brooklyn_note,cavs_note])
db.session.commit()