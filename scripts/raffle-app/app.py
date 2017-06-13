from flask import Flask, render_template, request, json, jsonify
from bhutils import rafflepy, utilities
import random, sys, argparse
app = Flask(__name__)

_USAGE = '''
app.py <data.csv> [--repeats] [--replace]

    Flags:
      --repeats
        If used, participants will be able to win multiple times, even
        after their name has been picked once

      --replace
        If used, participants tickets will be placed back into the raffle
        after their name is chosen. This only works if the '--repeats' flag
        is also chosen.
'''

# Parse command line arguments
parser = argparse.ArgumentParser(usage=_USAGE)
parser.add_argument("files",nargs=1)
parser.add_argument('--repeats', dest='repeats', action='store_true')
parser.add_argument('--replace', dest='replace', action='store_true')
args = parser.parse_args()

# Raffle game object to be populated at startup
raffle = None

# Main route used for home page
@app.route("/")
def main():
    return render_template('index.html')

# Called when button is pressed and suer wants a winner to be drawn
@app.route('/_get_winner')
def get_winner():
    global raffle
    choice = raffle.draw()
    if choice == None:
        choice = "Nobody Left..."
    return jsonify(result=choice.upper())

# Called when clear button is pressed
@app.route('/_clear')
def clear():
    return jsonify(result="???")

# Called when reset button is pressed
@app.route('/_reset')
def reset():
    global raffle
    del raffle
    generateRaffle()
    return jsonify(result="???")

def generateRaffle():
    global raffle

    try:
        # Load data from file
        with open(args.files[0], 'r') as fp:
            lines = fp.readlines()

        # Parse CSV file
        scores = {}
        for line in lines:
            (name, score) = line.split(",")
            scores[name] = int(score)
    except:
        raise ValueError("Could not parse data file")

    # Generate raffle
    raffle = rafflepy.Raffle(scores, repeats=args.repeats, replace=args.replace)

def main():
    generateRaffle()
    app.run(host='0.0.0.0', port=7000, debug=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(_USAGE)
    else:
        main()