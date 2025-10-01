from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mastermind_Logic # import logic file to use check_guess and new_game methods
app=Flask(__name__) # create Flask app

CORS(app, origins=["http://127.0.0.1:5500"]) #unused for now

# Initialize games dictionary as memory 
games = {} # May remove in favor of database integration later in development
next_id = 1 # Initialize next_id counter

@app.route('/') # Decorator indicating when to call home method 
def home():            
    return render_template('index.html'), 200 # Render index.html template


@app.route('/new_game', methods = ["POST"]) # Decorator indicating when to call new_game method
def new_game():
    global next_id
    
    game_id = next_id
    next_id+=1
    colors = ["Pink", "Orange", "Yellow", "Green", "Cyan", "Indigo"] # will not be hardcoded, see below
    maxGuesses = 10 # colors and maxGuesses are hardcoded for testing, but may add customization to web interface
    seqLength = 4
    
    game_data = mastermind_Logic.new_game(colors, maxGuesses, seqLength) # store all information resulting from new_game call in dictionary
    game_data["finished"] = False # add a state check for whether game is completed
    games[game_id] = game_data # initialize memory for given game_id
    
    
    # All non-rendering methods return the same dictionary structure for ease of parsing
    # data field for new_game contains game_id and a message string
    return jsonify({
        "success": True, 
        "data": {
            "game_id": game_id, 
            "message": "Game started.",
            "colors": game_data["colors"],
            "guesses": game_data["guesses"],
            "maxGuesses": game_data["maxGuesses"],
            "finished": game_data["finished"],
            "sequence": None, # do NOT send sequence when game is created
            "sequence_length": len(game_data["sequence"])
        }, 
        "error": None
    }), 201 # new game is created
    

@app.route('/guess', methods = ["POST"]) # Decorator indicating when to call new_game method
def guess():
    data = request.json # translates data from HTTP request, which Flask translates from json to a python dict

    game_id = data["game_id"] # saves game_id from data as an integer
    guess = data["guess"] # retrieves guess information from data as an array
    
    game = games.get(game_id) # retrieves information from memory corresponding to game_id extracted from data
    if not game: # returns an error if game cannot be found in memory
        return jsonify({"success": False, "data": None, "error": "Invalid game_id"}), 404
    
    # Determines accuracy of guess using check_guess and saves state to guess_data dict
    guess_data = mastermind_Logic.check_guess(guess, game["colors"], game["sequence"])
    
    if guess_data["status"]==1: # if guess is correct
        # increment guesses and indicate game is finished before returning
        game["guesses"]+=1
        game["finished"]=True
        return jsonify({
            "success": True,
            "data": {
                "game_id": game_id,
                "message": "Guess is valid and correct.",   
                "status": guess_data["status"], 
                "rightPos": guess_data["rightPos"], 
                "wrongPos": guess_data["wrongPos"],
                "colors": game["colors"],
                "guesses": game["guesses"],
                "maxGuesses": game["maxGuesses"],
                "finished": game["finished"],
                "sequence": game["sequence"], #reveal sequence for display, since game is over
                "sequence_length": len(game["sequence"])
            }, 
            "error": None
        }), 200 # guess is valid and accepted
    
    elif guess_data["status"]==-1: # if guess is invalid
        #don't change game status and return
        return jsonify({"success": False, "data": None, "error": "Invalid guess."}), 400
    
    else: # otherwise, successful guess 
        #increment guesses, then return
        game["guesses"]+=1
        
        if game["guesses"] == game ["maxGuesses"]:
            game["finished"] = True
            sequence = game["sequence"] # send sequence if game is over
        else:
            sequence = None # do not send sequence otherwise
        
        return jsonify({
            "success": True, 
            "data": {
                "game_id": game_id,
                "message": "Guess is valid but incorrect.",
                "status": guess_data["status"], 
                "rightPos": guess_data["rightPos"], 
                "wrongPos": guess_data["wrongPos"],
                "colors": game["colors"],
                "guesses": game["guesses"],
                "maxGuesses": game["maxGuesses"],
                "finished": game["finished"],
                "sequence": sequence,
                "sequence_length": len(game["sequence"])
            }, 
            "error": None
        }), 200 # guess is valid and accepted
    
# Entry point for dev server, debug=True tells Flask to reload app on changes
if __name__ == '__main__': 
    app.run(debug=True)
    