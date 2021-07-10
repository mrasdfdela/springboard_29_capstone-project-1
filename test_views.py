""" User view tests """

import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError

from models import db, connect_db, User, FavTeam, FavPlayer, NoteTeam, NotePlayer
from test_helper import addFavTeam, addFavPlayers, addNoteTeam, addNotePlayers

os.environ['DATABASE_URL'] = "postgresql:///ball-do-lie"
from app import CURR_USER_KEY, app

app.config['WTF_CSRF_ENABLED'] = False

class UserModelCreateTestCase(TestCase):
    """Test user models"""
    def setUp(self):
        """Create test client, add sample data"""
        db.drop_all()
        db.create_all()
        
        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="fort_knox") 
        db.session.commit()

        addFavTeam()
        addFavPlayers()
        addNoteTeam()
        addNotePlayers()
        db.session.commit()

        self.client = app.test_client()
        db.session.expire_on_commit=False

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_index(self):
        """View homepage"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            """Homepage"""
            resp = c.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<ul class="navbar-nav ms-auto me-5 mb-2 mb-lg-0"">', html)
            self.assertIn(f'<h1>Latest Games</h1>', html)

            """User page"""
            resp = c.get('/user/1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"<h1>testuser\'s Favorites</h1>", html)
            self.assertIn(f'<a href="/player/140">', html)
            self.assertIn(f'<a href="/team/27">', html)

            """Logout and view"""            
            new_resp = c.get('/logout',follow_redirects=True)
            html = new_resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<a class="nav-link active" aria-current="page" href="/login">Log in</a>', html)

            last_resp = c.get('/signup')
            html = last_resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<h1>Sign up!</h1>', html)


    def test_game(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            resp = c.get('/game/1')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<p>Final Score</p>', html)
            self.assertIn(f'<table class="table">', html)

    def test_team(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
    
            resp = c.get('/team/27')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<h1>San Antonio Spurs', html)
            self.assertIn(f'Go Spurs Go!', html)
    
    def test_player(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
    
            resp = c.get('/player/140')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<p>Position: ', html)
            self.assertIn(f'easy money sniper', html)


    def test_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
    
            resp = c.get('/player/140')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<p>Position: ', html)
            self.assertIn(f'easy money sniper', html)