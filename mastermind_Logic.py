import random # used for random.choices function to generate sequence

def main():

    proceed=True # used to loop new_game until user chooses to quit
    colors=["Orange", "Yellow", "Green", "Cyan", "Indigo", "Pink"] # initialize colors
    maxGuesses=10 # initialize maxGuesses

    prompt = "Enter a sequence of four of the following colors separated by spaces. Options are: " \
        "\nOrange, Yellow, Green, Cyan, Indigo, Pink\n"
        
    play_again_prompt = "\n Would you like to play again? y/n \n"

    while proceed: # loops until user quits
        data=new_game(colors, maxGuesses) # creates a new game and stores data for it in a dictionary
        complete = 0 # initializes game as incomplete
        sequence = data["sequence"] # stores sequence from new_game data in an array
        guesses = data["guesses"] # stores guesses from new_game data in an array, starts at zero
        print(sequence) #DEBUGGING ONLY
        print(prompt)


        while guesses < maxGuesses:
            # invalid=False
            attempt=(input("What is your guess? ")).split() # Take user input for guess
            determined=check_guess(attempt, colors, sequence) # Call check_guess to parse input and store result in determined dict
            status=determined["status"] # extracts status from determined
            if status == -1: # handle invalid guesses
                print(f"Invalid guess, you still have {maxGuesses-guesses} guesses remaining.")
                print(prompt)
                continue
            elif status==1: # handle correct guesses
                guesses+=1
                print(f"You correctly guessed the sequence in {guesses} guesses!")
                complete=1
                break
                # quit()
            elif status==0: #handle incorrect guesses
                rightPos=determined["rightPos"]
                wrongPos=determined["wrongPos"]
                guesses+=1
                print(f"Your attempt has {rightPos} elements placed correctly and {wrongPos} elements in the wrong position.")
                print(f"You have {maxGuesses-guesses} guesses remaining.\n")
            else: # should never happen, for debugging
                print("Unknown Error Occurred.")
                quit()
        if complete==0: # Check if game has ended following incorrect guess
            print("Ran out of guesses! The sequence was: \n")
            print(sequence)
        cont = ""
        while cont != "y" and cont != "n": # loop until user requests to continue or end
            cont=input(play_again_prompt)
            if cont == "y":
                break
            elif cont == "n":
                proceed=False
                break
            else: # catch invalid input
                print("Invalid input.")
                continue
    
def new_game(colors, maxGuesses): # initializes game data and returns data dict
    sequence = random.choices(colors, k=4)
    guesses = 0
    maxGuesses = maxGuesses
    data = {"colors": colors, "sequence": sequence, "guesses": guesses, "maxGuesses": maxGuesses}
    return data
    
            
def check_guess(guess, colors, sequence): # checks if guess is correct
    if invalid(guess, colors): # calls invalid and returns if guess is invalid
        return {"status": -1, "rightPos": 0, "wrongPos": 0}
    else: # checks how many entries are in the right or wrong position
        index=0 # used for first iteration and inner while loop of second iteration
        rightPos=0
        wrongPos=0
        blacklist=[False, False, False, False] # used to prevent double-counting for wrongPos
        #First iteration to check for colors in correct position
        for item in guess:
            if item == sequence[index]:
                rightPos += 1
                blacklist[index]=True # blacklists colors in correct position so they do not double count
                index +=1
            else:
                index +=1

        #Second iteration uses blacklist to determine number of colors in incorrect position
        for i, item in enumerate(guess):
            if item != sequence[i]:
                index=0 # reinitialize index, may change to different variable for readability
                while index<4:
                    if item == sequence[index] and blacklist[index] == False:
                        blacklist[index] = True # blacklists entries as they are counted so they do not double count
                        wrongPos +=1
                        break
                    index+=1

        if rightPos==4 and wrongPos==0: # checks if answer is correct and returns
            return {"status": 1, "rightPos": rightPos, "wrongPos": wrongPos}
        else:
            return {"status": 0, "rightPos": rightPos, "wrongPos": wrongPos}

        

def invalid(guess, colors): # checks if guesses are valid
    if len(guess)!=4:
        return True
    else:
        for item in guess:
            if item not in colors:
                return True
        return False
            
if __name__ == "__main__": # tells program to run main
    main()  

