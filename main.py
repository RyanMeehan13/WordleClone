import tkinter as tk
#import pynput as pyn
from resources import *
# TODO:
# -Display a window that looks like the wordle site DONE
# -Get the window to respond to resizing DONE
# -allow the user to enter text used for the game DONE
# -change the window based on user choices
#    -IE: Color of cells based on letter choice
#    -display entered chars in the cells DONE

fName = "wordle-answers-alphabetical.txt"
answerList = createList(fName)
hiddenWord = getHiddenWord(answerList)


BOX_GREY = '#3f3f3f'
FRAME_GREY = '#2a2a2a'
YELLOW = '#FDDA0D'
GREEN = '#00C72B'
font_title = ('Helvetica', 30, 'bold')
font_box = ('Helvetica', 20, 'bold')
window = tk.Tk()
window.configure(bg='black')
window.geometry('800x800')

class Counter:
    def __init__(self):
        self.i=1
        self.j=0
    def incrementI(self):
        self.i+=1
    def decrementI(self):
        self.i-=1
    def incrementJ(self):
        self.j+=1
    def decrementJ(self):
        self.j-=1
    def resetI(self):
        self.i =1
    def resetJ(self):
        self.j =0

myCounter = Counter()


top = tk.Frame(master=window, borderwidth=1, width=100, height=5, bg='black')
top.grid(row=0, columnspan=5, padx=1, pady=1)
title = tk.Label(master=top, text=f"WORDLE CLONE", width=100, height=1, font=font_title, bg='black', fg='white')
title.pack()

# create a dictionary of cells
cells = {}

for i in range(1, 7):
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 5):
        window.columnconfigure(j, weight=1, minsize=10)
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=0,
            width=10,
            height=10,
            bg='black'
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text="", width=20, height=10, font=font_box, bg=BOX_GREY,
                         fg='white')
        cells[(i, j)] = label  # store every label in a dictionary with a coordinate tuple as a key

        label.pack(padx=5, pady=5)

def showErrorMsg():
    errWin = tk.Tk()
    errWin.configure(bg = 'black')
    errWin.geometry('300x100')
    errLabel = tk.Label(master = errWin, text = "Error, that word is \nnot in dictionary.\nTry another word.",
                        bg = 'black',
                     fg = 'white', font = font_box)
    errLabel.pack(padx=5,pady=5)
    errWin.mainloop()

def showGameOverMsg(win):
    if(win):
        gameOverString = "Congratulations, \nyou won!"
    else:
        gameOverString = f"Better luck next time,\nthe word was {hiddenWord}."
    errWin = tk.Tk()
    errWin.configure(bg = 'black')
    errWin.geometry('300x100')
    errLabel = tk.Label(master = errWin, text = gameOverString,
                        bg = 'black',
                     fg = 'white', font = font_box)
    errLabel.pack(padx=5,pady=5)
    errWin.mainloop()

def handle_key(event, counter = myCounter, dict = cells):
    win = False
    c = event.char
    i = counter.i
    #print(i)
    j = counter.j
    #print(j)
    #print(c)
    #print("--------")
    if(c==' ' or c==''or c=='\n' or c=='\t' ):
        x=1 #placeholder. I want to do nothing here
    elif(c=='.'): #this signifies the end of a row, go to next row #We can change this to the 'enter' identifier once we get it
        if(j>=4 and dict[(i,4)]['text']!='' and dict[(i,4)]['text']!=' '):
            # get the chars in this row into a string
            guess = ""
            for q in range(0,5):
                guess+=dict[(i,q)]['text']
            #we now have the guess. Validate it
            if(validateGuess(guess, myDictionary)): #if yes -> bad input
                showErrorMsg()


            else: #good guess
                #We need to check guess, change tiles and move to next row
                line = checkGuess(guess, hiddenWord)
                for v in range(0,5):
                    if(line[v]=='!'):
                        dict[(i,v)]['bg']=GREEN
                    elif(line[v]=='?'):
                        dict[(i,v)]['bg']=YELLOW
                if(line=='!!!!!'):
                    win = True
                    showGameOverMsg(win)
                    window.destroy()
                elif(i==6 and j==5):
                    window.destroy()
                    showGameOverMsg(win)
                    window.destroy()

                counter.incrementI()
                counter.resetJ()
    elif(c=='\b'): #if c is a backspace
        counter.decrementJ()
        j = counter.j
        dict[(i, j)]['text'] = " "
    else: #This means it is a normal char
        dict[(i, j)]['text'] = c
        counter.incrementJ()


window.bind("<Key>", handle_key)


#cells[(1,3)]['bg'] = YELLOW
#cells[(3,2)]['bg'] = GREEN
#cells[(5,1)]['bg'] = YELLOW
#cells[(4,4)]['bg'] = GREEN

window.mainloop()






