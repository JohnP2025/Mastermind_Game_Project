import random

colors=["Orange", "Yellow", "Green", "Cyan", "Indigo", "Pink"]

maxGuesses=10
invalid=False

prompt = "Enter a sequence of four of the following colors separated by spaces. Options are: " \
    "\nOrange, Yellow, Green, Cyan, Indigo, Pink\n"

sequence = random.choices(colors, k=4)

guesses = 0

print(sequence) #DEBUGGING ONLY
print(prompt)

while guesses < maxGuesses:
    invalid=False
    attempt=(input("What is your guess? ")).split()

    if len(attempt)!=4:
        print(f"Invalid guess, you still have {maxGuesses-guesses} guesses remaining.")
        print(prompt)
        continue
    else:
        index=0
        rightPos=0
        wrongPos=0
        blacklist=[False, False, False, False]
        #First iteration to check for colors in correct position
        for item in attempt:
            if item not in colors:
                invalid=True
                break
            elif item == sequence[index]:
                rightPos += 1
                blacklist[index]=True
                index +=1
            else:
                index +=1

        #Second iteration uses blacklist to determine number of colors in incorrect position

        if invalid:
            print(f"Invalid guess, you still have {maxGuesses-guesses} guesses remaining.")
            print(prompt)
            continue


        for i, item in enumerate(attempt):
            if item != sequence[i]:
                index=0
                for entry in sequence:
                    if item == sequence[index] and blacklist[index] == False:
                        blacklist[index] = True
                        wrongPos +=1
                        break
                    index+=1

        guesses+=1
        if rightPos==4 and wrongPos==0:
            print(f"You correctly guessed the sequence in {guesses} guesses!")
            quit()
        else:
            print(f"Your attempt has {rightPos} elements placed correctly and {wrongPos} elements in the wrong position.")
            print(f"You have {maxGuesses-guesses} guesses remaining.\n")

print("Ran out of guesses! The sequence was: \n")
print(sequence)
