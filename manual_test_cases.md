# Manual test cases for version 1 of Mastermind game project.

## Environment 
Python 3.13.7. Tested on Windows 11, PowerShell terminal.  

---  

## INVALID INPUT  

#### Test Case 1 - Checking invalid input of length less than 4  
Input: Cyan Orange Pink  
Sequence: ['Green', 'Green', 'Pink', 'Cyan']  
Expected Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Produced Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Result: Pass  

#### Test Case 2 - Checking invalid input of length greater than 4  
Input: Orange Green Pink Cyan Indigo  
Sequence: ['Orange', 'Cyan', 'Indigo', 'Pink']  
Expected Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Produced Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Result: Pass  

#### Test Case 3 - checking invalid input consisting of unallowed colors/phrases  
Input: Red Magenta Aqua Jade  
Sequence: ['Yellow', 'Indigo', 'Orange', 'Orange']  
Expected Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Produced Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Result: Pass  

#### Test Case 4 - checking invalid input with separator other than space  
Input: Yellow.Orange.Indigo.Cyan  
Sequence: ['Cyan', 'Cyan', 'Pink', 'Pink']  
Expected Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Produced Output:  
- Message: `Invalid guess, you still have 10 guesses remaining.`

Result: Pass  

---  

## SUCCESSFUL INCORRECT GUESS  

#### Test Case 5 - checking valid guess with no correct elements  
Input: Cyan Cyan Green Indigo  
Sequence: ['Orange', 'Orange', 'Yellow', 'Pink']  
Expected Output:  
- Message: `Your attempt has 0 elements placed correctly and 0 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Produced Output:  
- Message: `Your attempt has 0 elements placed correctly and 0 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Result: Pass  

#### Test Case 6 - checking valid guess with one element in wrong position  
Input: Pink Orange Orange Indigo  
Sequence: ['Indigo', 'Cyan', 'Green', 'Yellow']  
Expected Output:  
- Message: `Your attempt has 0 elements placed correctly and 1 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Produced Output:  
- Message: `Your attempt has 0 elements placed correctly and 1 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Result: Pass  

#### Test Case 7 - checking valid guess with one element in wrong position and one in right position  
Input: Pink Green Orange Indigo  
Sequence: ['Yellow', 'Green', 'Yellow', 'Pink']  
Expected Output:  
- Message: `Your attempt has 1 elements placed correctly and 1 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Produced Output:  
- Message: `Your attempt has 1 elements placed correctly and 1 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Result: Pass  

#### Test Case 8 - checking valid guess with only one element in right position, but more instances to detect double-counting  
Input: Yellow Yellow Yellow Yellow  
Sequence: ['Yellow', 'Green', 'Cyan', 'Orange']  
Expected Output:  
- Message: `Your attempt has 1 elements placed correctly and 0 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Produced Output:  
- Message: `Your attempt has 1 elements placed correctly and 0 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Result: Pass  

#### Test Case 9 - checking valid guess with two elements in right position and two elements in wrong position  
Input: Green Green Indigo Cyan  
Sequence: ['Green', 'Green', 'Cyan', 'Indigo']  
Expected Output:  
- Message: `Your attempt has 2 elements placed correctly and 2 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Produced Output:  
- Message: `Your attempt has 2 elements placed correctly and 2 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Result: Pass  

#### Test Case 10 - checking valid guess with three elements in correct position and no elements in wrong position  
Input: Indigo Pink Indigo Cyan  
Sequence: ['Indigo', 'Pink', 'Indigo', 'Green']  
Expected Output:  
- Message: `Your attempt has 3 elements placed correctly and 0 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Produced Output:  
- Message: `Your attempt has 3 elements placed correctly and 0 elements in the wrong position.`  
- Message: `You have 9 guesses remaining.`

Result: Pass  

---  

## GAME OVER CONDITIONS  

#### Test Case 11 - checking valid correct guess  
Input: Indigo Orange Indigo Cyan  
Sequence: ['Indigo', 'Orange', 'Indigo', 'Cyan']  
Expected Output:  
- Message: `You correctly guessed the sequence in 1 guesses!`

Produced Output:  
- Message: `You correctly guessed the sequence in 1 guesses!`
  
Result: Pass  

#### Test Case 12 - checking that game ends after maxGuesses is exceeded  
Input: Indigo Orange Indigo Cyan  
Sequence: ['Yellow', 'Green', 'Orange', 'Indigo']  
Expected Output:  
- Message: `Ran out of guesses! The sequence was:`  
- Message: `['Yellow', 'Green', 'Orange', 'Indigo']`

Produced Output:  
- Message: `Ran out of guesses! The sequence was:`  
- Message: `['Yellow', 'Green', 'Orange', 'Indigo']`

Result: Pass  

---  

## Future Testing  
Future versions will migrate testing to automated pytest unit tests.  
