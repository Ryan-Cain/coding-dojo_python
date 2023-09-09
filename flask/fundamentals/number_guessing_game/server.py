# This is a WIP

from flask import Flask, session, request, redirect, render_template
import random

app = Flask(__name__)
app.secret_key = 'shh this is a secret'

@app.route('/')
def game():
    if not 'game_started' in session:
        print('game started now')
        session['game_started'] = True
    if not 'game_won' in session:
        session['game_won'] = False
    if not 'guess_high' in session:
        session['guess_high'] = True
    if not 'number' in session:
        session['number'] = random.randint(1, 101)
    return render_template('index.html', game_won=session['game_won'])

@app.route('/guess', methods=['POST', 'GET'])
def guess():
    guess = int(request.form['guess'])
    session['game_started'] = True
    if guess == session['number']:
        session['game_won'] = True
    elif guess > session['number']:
        session['guess_high'] = True
    else:
        session['guess_high'] = False
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)