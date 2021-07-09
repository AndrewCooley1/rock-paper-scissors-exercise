# game.py

import random


print("Rock, Paper, Scissors, Shoot!")


#Ask for user input
#source: https://docs.python.org/3/library/functions.html#input

x = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(x)

#validate user input


if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()


print("user chose: ",x)

#generate computer choice
#https://docs.python.org/3/library/random.html
#source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list


valid_options = ["rock", "paper", "scissors"] #list

c = random.choice(valid_options)
print("COMPUTER Chose:", c)
#determine the winner
