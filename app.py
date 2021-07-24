from boggle import Boggle
from flask import Flask, render_template, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "DEUSVULT"
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def board_screen():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template('board.html', board=board)
