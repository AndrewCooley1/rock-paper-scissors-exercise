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


print("User chose: ",x)

#generate computer choice
#https://docs.python.org/3/library/random.html
#source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list


valid_options = ["rock", "paper", "scissors"] #list

c = random.choice(valid_options)
print("Computer Chose:", c)
#determine the winner

#convert rock, paper and scissor into numbers
if (x) == "rock":
    x = 0
elif (x) == "paper":
    x = 1
elif (x) == "scissors":
    x = 2

#determine if we won or lost
if (x) == 0: #rock
    if (c) == "rock":
        print ("It's s tie! Spin again")
if (x) == 0: #rock
    if (c) == "paper":
        print ("You lose, try again!")
if (x) == 0: #rock
    if (c) == "Scissors":
        print ("You win!")











  #  elif (x) == 1: #paper
   #     print ("Paper covers rock, you lose!")
    #elif (x) == 2: #scissors
     #   print ("Rock beats Paper!")

