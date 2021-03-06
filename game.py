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
#if (x) == "rock":
#    x = 0
#if (x) == "paper":
#    x = 1
#if (x) == "scissors":
#    x = 2

#determine if we won or lost
#inspired by losely https://www.geeksforgeeks.org/python-if-else/#if-else
#user picks rock
if x == c:
    print("It's a tie, try again")
elif x == "rock" and c == "paper":
    print ("You Lose! Play again")
elif x ==  "rock" and c == "scissors":
    print ("You win! Yay!")
elif x == "paper" and c == "rock":
    print ("You win! Yay!")
elif x == "paper" and c == "scissors":
    print ("You lose! Better luck next time.")
elif x == "scissors" and c == "rock":
    print ("You lose! Sorry!")
elif x == "scissors" and c == "paper":
    print ("You win! Yay!")
