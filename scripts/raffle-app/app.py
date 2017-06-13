from flask import Flask, render_template, request, json, jsonify
from bhutils import rafflepy
import random, sys
app = Flask(__name__)

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
    print("draw!")
    choice = raffle.draw()
    return jsonify(result=choice)

def main(datafile):
    global raffle

    try:
        # Load data from file
        with open(datafile, 'r') as fp:
            lines = fp.readlines()

        # Parse CSV file
        scores = {}
        for line in lines:
            (name, score) = line.split(",")
            scores[name] = int(score)
    except:
        raise ValueError("Could not parse data file")

    # Generate raffle
    print(scores)
    raffle = rafflepy.Raffle(scores)

    app.run(host='0.0.0.0', port=7000, debug=False)

def usage():
    print("python raffle.py [data.csv]")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    else:
        main(sys.argv[1])