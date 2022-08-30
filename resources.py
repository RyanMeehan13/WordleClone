import random
from dictionary import *

#So we are at the first char
# we check first if that char=first chaar in hidden
#if not, check if that char is in hidden at all
# if both false, then _.

def createList(fName):
    with open(fName) as file:
        answerList = file.read().splitlines()
    return answerList

def getHiddenWord(answerList):
    num = random.randrange(0,len(answerList))
    word = answerList[num]
    return word

def checkGuess(guess, hiddenWord):
    line = ""
    lGuess = guess.lower() #normalize input
    lHidden = hiddenWord.lower() #normalize hidden
    for i in range(0, len(lGuess)):
        #We are now looping through the guess, letter by letter
        if(lGuess[i] == lHidden[i]):
            #This is a green tile.
            #Chars match
            line +="!"
        elif(lGuess[i] in lHidden):
            #This is a yellow tile.
            #Char does not match, but is in the hidden word.
            line+="?"
        else:
            #This is a grey tile.
            #This means that the char does not appear in word
            line+="_"

    return line


def validateGuess(guess, dictionary):
    guess = guess.lower()
    if (len(guess) != 5):
        #print("Guess must be 5 letters long.")
        return True
    elif(guess in dictionary):
        return False #is guess bad?
    else:
        #print("Invalid guess. Word is not in dictionary.")
        return True #is guess bad?