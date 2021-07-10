""" User model tests """

import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError

from models import db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer
from test_helper import addDuplicateUser, addUsers, addThirdUser, addNoteTeam, addNotePlayers

os.environ['DATABASE_URL'] = "postgresql:///ball-do-lie"
from app import app

class UserModelCreateTestCase(TestCase):
    """Test user models"""
    def setUp(self):
        """Create test client, add sample data"""
        db.drop_all()
        db.create_all()
        addUsers()
        db.session.commit()
        self.client = app.test_client()
    
    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
    
    def test_user_model(self):
        """Does the basic user model work?"""
        user = User.query.first()
        self.assertEqual(len(user.favplayers), 0)
        self.assertEqual(len(user.favteams), 0)
        self.assertEqual(user.username,"testuser")
        self.assertEqual(user.email,"test@test.com")
    
    def test_user_create(self):
        """Does the signup class method work?"""
        addThirdUser()

        self.assertEqual(len(User.query.all()), 3)

        user = User.query[-1]
        self.assertEqual(user.username,"latest_user")
        self.assertEqual(user.email,"latest@latest.com")

    def test_user_create_duplicate(self):
        with self.assertRaises(IntegrityError):
            addDuplicateUser()

    def test_user_authetication(self):
        """Has authentication worked correctly?"""
        addThirdUser()

        user = User.query[-1]
        self.assertNotEqual(User.password,"fort_knox")
        self.assertEqual(User.authenticate("latest_user","fort_knox"),user)

class FavsTestCase(TestCase):
    """Test Favorite Team and Players"""
    def setUp(self):
        """Create test client, add sample data"""
        db.drop_all()
        db.create_all()
        addUsers()
        db.session.commit()
        self.client = app.test_client()
    
    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_add_favorite_team(self):
        fav_team = FavTeam(user_id=1,team_id=27)
        db.session.add(fav_team)
        db.session.commit()

        user = User.query.first()
        fav_team = user.favteams[0]

        self.assertEqual(fav_team.team_id, 27)
        self.assertEqual(len(user.favteams), 1)

    def test_add_favorite_player(self):
        fav_p1 = FavPlayer(user_id=1,player_id=237)
        fav_p2 = FavPlayer(user_id=1,player_id=228)
        db.session.add_all([fav_p1,fav_p2])
        db.session.commit()

        user = User.query.first()
        fav_player = user.favplayers[0]

        self.assertEqual(fav_player.player_id, 237)
        self.assertEqual(len(user.favplayers), 2)

class NotesTestCase(TestCase):
    """Test Favorite Team and Players"""
    def setUp(self):
        """Create test client, add sample data"""
        db.drop_all()
        db.create_all()
        addUsers()
        db.session.commit()
        self.client = app.test_client()
    
    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_note_team(self):
        note = addNoteTeam()
        user = User.query.first()
        user_note = user.notesteams[0]

        self.assertEqual(user_note, note)
        self.assertEqual(len(user.notesteams), 1)

    def test_note_player(self):
        notes = addNotePlayers()

        user = User.query.first()
        user_note = user.notesplayers[0]

        self.assertEqual(user_note, notes[0])
        self.assertEqual(len(user.notesplayers), 2)