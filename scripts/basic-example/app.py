from flask import Flask, render_template, request, json, jsonify
from bhutils import rafflepy, utilities
import random, sys, argparse, json
app = Flask(__name__)

_USAGE = '''
app.py <db.json>
'''

_DEBUG = True
def debug_print(msg):
    if _DEBUG:
        print(msg)

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

# Parse command line arguments
parser = argparse.ArgumentParser(usage=_USAGE)
parser.add_argument("files",nargs=1)
args = parser.parse_args()

# Called when approve button is pressed
@app.route('/_approve_btn_pressed')
def approve_btn_pressed():
    return jsonify(result="success.")

# Main route used for home page
@app.route("/")
def mainpage():
    debug_print("Rendering main page.")
    return render_template('index.html')

def main():
    global game
    game = Cognomic(args.files[0])
    app.run(host='0.0.0.0', port=7000, debug=False)

if __name__ == "__main__":
    main()