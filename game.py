# game.py

import random



print("Rock, Paper, Scissors, Shoot!")


#Ask for user input
#source python docs

x = input("Please choose one of 'rock', 'paper', 'scissors'")
print (x)
#validate user input


if (x =="rock") or (x == "paper") or (x == "scissors"):
    print("valid")
else:
    print("oops, invalid, please try again")
    exit()

print(user chose ("x")

#generate computer choice
#source from stackoverflow


valid_options = ["rock", "paper", "scissors"] #list

c = (random.choice(valid_options))
#determine the winner
