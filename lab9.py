# Lab 9
# Author: Bo Rogers

import random

print("Let's play Robot, Pirate, Ninja, Monkey, Zombie")
playAgain = "y"
score = 0
players = ("robot", "pirate", "ninja", "monkey", "zombie")

while playAgain == "y" or playAgain == "yes":
    compAns = random.choice(players)
    ans = input("Do you want to be a Robot, Pirate, Ninja, Monkey, Zombie?: ")
    

    if compAns == "robot" and ans == "pirate":
       print("Computer Wins")
    elif compAns == "zombie" and ans == "robot":
       print("Computer Wins")
    elif(compAns == ans):
        print("Tie")
    
    playAgain = input("Would you like to play again? y(yes) or n(no): ").strip().lower()

print("Your score was: " + str(score))
print("Goodbye")