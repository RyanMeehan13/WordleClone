#imports
from resources import * #maybe change later. Do we need everything??
fName = "wordle-answers-alphabetical.txt"

#get the answer list from file

answerList = createList(fName)

#get a random hidden word from the list

hiddenWord = getHiddenWord(answerList)

#ask for guess
print("Welcome to my Wordle clone!")
print("You have 6 guesses to find the hidden word.")
print("A ! means that that character is in the word and in the correct position.")
print("A ? means that that character is in the word and is not in the correct position.")
print("A _ means that that character is not in the word.")


badGuess = True
while(badGuess):
    guess = input("Please enter a guess:\n")
    badGuess = validateGuess(guess, myDictionary)



line = checkGuess(guess, hiddenWord)
print(line)
wrong = True
if(line == "!!!!!"):
        wrong = False
i =0
while( i<5 and wrong):
    guess = input("\n")
    line = checkGuess(guess, hiddenWord)
    print(line)
    if (line == "!!!!!"):
        wrong = False
        break
    i+=1

if(not wrong):
    print("Congratulations! You guessed the hidden word was",hiddenWord)
else:
    print("Better luck next time, the hidden word was",hiddenWord )

