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

#convert user pick of rock, paper and scissor into numbers
if (x) == "rock":
    x = 0
if (x) == "paper":
    x = 1
if (x) == "scissors":
    x = 2

#determine if we won or lost
#inspired by losely https://www.youtube.com/watch?v=ZDiPqfFF7pw
#user picks rock
if (x) == 0: #rock
    if (c) == "rock":
        print ("It's s tie! Spin again")
if (x) == 0: #rock
    if (c) == "paper":
        print ("You lose, try again!")
if (x) == 0: #rock
    if (c) == "Scissors":
        print ("You win!")

#user picks Paper
if (x) == 1: #paper
    if (c) == "rock":
        print ("You win!")
if (x) == 1: #Paper
    if (c) == "paper":
        print ("It's a tie, try again!")
if (x) == 1: #paper
    if (c) == "Scissors":
        print ("You lose!")

#user picks scissors
if (x) == 2: #scissors
    if (c) == "rock":
        print ("You lose!")
if (x) == 2: #scissors
    if (c) == "paper":
        print ("You win!")
if (x) == 2: #scissors
    if (c) == "Scissors":
        print ("It's a tie, try again!")









