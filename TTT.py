from tkinter import *
import random


def next_turn(row, column):
    global player
    if buttons[row][column]['text']=="" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]

                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]

                label.config(text=(players[0]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie")







def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    elif buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return True

    else:
        return False



window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 50))
label.pack(side="top")


frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]= Button(frame, text="", font=('consolas', 50), width="5", height="2",
                                     command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()
