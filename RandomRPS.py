import random

while True:
    P_choices = ["rock", "paper", "scissors"]

    AI = random.choice(P_choices)
    Human = None

    while Human not in P_choices:
        print("rock, paper, scissors? (please pick a relevant option)")
        Human = input("ROCK,PAPER,SCISSORS => ").lower()

    if Human == AI:
        print("AI - " + AI)
        print("Human - " + Human)
        print("IT'S A TIE!")

    elif Human == "rock" and AI == "paper" or Human == "paper" and AI == "scissors" or Human == "scissors" and AI == "rock":
        print("AI - " + AI)
        print("Human - " + Human)
        print("AI wins!")

    elif Human == "paper" and AI == "rock" or Human == "scissors" and AI == "paper" or Human == "rock" and AI == "scissors":
        print("AI - " + AI)
        print("Human - " + Human)
        print("You win!")

    restart = input("Do you want to play again? (yes/no) :- ")
    if restart != "yes":
        break

print("THANKS FOR PLAYING!")

