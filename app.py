from boggle import Boggle
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456789"
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def board_screen():
    '''This is the home page of the site. When the site loads, make a boggleboard and add it to the session. show user the html template title  'board'. '''
    board = boggle_game.make_board()
    session["board"] = board
    return render_template('board.html', board=board)

@app.route('/check-guess', methods=['POST'])
def check_word():
    '''when the user enters a guess, this handles the post request. the AJAX POST request is sent here with a 'guess' JSON. This function grabs that guess, and checks to see if it is a valid word. It provides the corresponding return message, reformatting it from the JSON object.
    '''

    # grab the guessed word from the AJAX POST request
    guess = request.json['guess']

    # recall the board from session
    board = session['board']

    # prepare a json response by checking if the guess is a valid word on the board
    json_response = boggle_game.check_valid_word(board, guess)

    # respond to AJAX using a jsonified element
    return jsonify(json_response)


@app.route('/record-score', methods=['POST'])
def record_score():
    ''' once game is over, take the score on the front end and store it in session. also, add 1 to the play count. '''

    # check if this is the first time playing game
    if session.get('num_of_plays') is None:
        session['num_of_plays'] = 0
        session['highest_score'] = 0

    # add 1 to num of plays
    session['num_of_plays'] += 1

    # update highest score if it has changed
    new_score = int(request.json['score'])
    if new_score > session['highest_score']:
        session['highest_score'] = new_score

    return jsonify(new_score)