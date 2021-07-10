from models import db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer

def addUsers():
    u1 = User(
        email="test@test.com",
        username="testuser",
        password="HASHED_PASSWORD")

    u2 = User(
    email="trial@trial.com",
    username="trialuser",
    password="CODED_PASSWORD")
    
    db.session.add_all([u1,u2])
    db.session.commit()

def addThirdUser():
    User.signup(
      username="latest_user",
      email="latest@latest.com",
      password="fort_knox"
    )
    db.session.commit()

def addDuplicateUser():
    User.signup(
      username="testuser",
      email="reduce@reuse.com",
      password="recycle"
    )
    db.session.commit()

def addFavTeam():
    fav = FavTeam(user_id=1,team_id=27)
    db.session.add(fav)
    db.session.commit()
    return fav

def addFavPlayers():
    fav_p1 = FavPlayer(user_id=1,player_id=140)
    fav_p2 = FavPlayer(user_id=1,player_id=192)
    db.session.add_all([fav_p1,fav_p2])
    db.session.commit()
    return [fav_p1, fav_p2]

def addNoteTeam():
    note = NoteTeam(user_id=1,team_id=27,note="Go Spurs Go!")
    db.session.add(note)
    db.session.commit()
    return note

def addNotePlayers():
    note_p1 = NotePlayer(user_id=1,player_id=140,note="easy money sniper")
    note_p2 = NotePlayer(user_id=1,player_id=192,note="the beard")
    db.session.add_all([note_p1,note_p2])
    db.session.commit()
    return [note_p1, note_p2]