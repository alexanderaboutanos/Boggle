from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):
    def test_board_screen(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            print(html)

            self.assertIsNotNone(session['board'])
            self.assertIn("<h1>Let's Play Boggle!</h1>", html)
            self.assertEqual(res.status_code, 200)
            

    def test_check_word(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(res.status_code, 200)

    def test_record_score(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(res.status_code, 200)


