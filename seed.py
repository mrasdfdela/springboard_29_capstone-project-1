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