from flask import Flask, render_template, flash, request, json, jsonify, session, abort, redirect
from bhutils import rafflepy, utilities
import random, sys, argparse, json, os
app = Flask(__name__)

_DEBUG = True
def debug_print(msg):
    if _DEBUG:
        print(msg)

_USAGE = '''
app.py <db.json>
'''

# Parse command line arguments
parser = argparse.ArgumentParser(usage=_USAGE)
parser.add_argument("files",nargs=1)
args = parser.parse_args()


#=================================================================
#===================     GAME LEVEL      =========================
#=================================================================


# Game object to be populated at startup
game = None

class Cognomic():
    def __init__(self, db=None):
        self.data = {}
        if db != None:
            self.loadGame(db)

    def loadGame(self, db_file):
        try:
            # Load data from file
            with open(db_file, 'r') as fp:
                self.data = json.load(fp)
                debug_print("Data file loaded.")
        except:
            raise ValueError("ERROR: Cannot read json db file.")




#=================================================================
#===================     APP LEVEL      ==========================
#=================================================================

# Handles login screen and authenticating users
@app.route('/login', methods=['POST'])
def do_admin_login():
    debug_print(request.form['username'])
    players = [player["name"] for player in game.data["players"]]
    if request.form['username'] in players:
        session['user'] = request.form['username']
    else:
        flash('Not an eligible player!')
    return mainpage()

# Called when approve button is pressed
@app.route('/_approve_btn_pressed')
def approve_btn_pressed():
    return jsonify(result="success.")

# Called when approve button is pressed
@app.route('/_decline_btn_pressed')
def decline_btn_pressed():
    return jsonify(result="success.")

# Called when approve button is pressed
@app.route('/_clear_btn_pressed')
def clear_btn_pressed():
    return jsonify(result="success.")

# Main route used for home page
@app.route("/")
def mainpage():
    if not session.get('user'):
        return render_template('login.html')

    debug_print("Rendering main page.")
    return render_template('index.html', gamedata=game.data)

def main():
    global game
    game = Cognomic(args.files[0])
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)

if __name__ == "__main__":
    main()