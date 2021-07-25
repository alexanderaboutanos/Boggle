from boggle import Boggle
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "DEUS_VULT"
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def board_screen():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template('board.html', board=board)

@app.route('/check-guess', methods=['POST'])
def check_word():

    # grab the guessed word from the AJAX POST request
    guess = request.json['guess']

    # recall the board from session
    board = session['board']

    # prepare a json response by checking if the guess is a valid word on the board
    json_response = boggle_game.check_valid_word(board, guess)

    # respond to AJAX using a jsonified element
    return jsonify(json_response)
