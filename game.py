# this is the "game.py" file...
# Call to start game
from random import Random, random


print("Welcome to Rock, Paper, Scissors!")

#Prompt user decision
#move = ["Rock", "Paper", "Scissors"]
print("Choose your move from either Rock, Paper or Scissors")
x = input()
print("---------------------------------")
if (x == "ROCK" or x == "Rock" or x =="rock"):
    print("Rock, Paper, Scissors and shoot!!")
    print("Your move: Rock")
    import random
    move = random.choice(["Rock", "Paper", "Scissors"])
    print ("Computer's move: " + move)
    print("---------------------------------")
    if (move == "Rock"):
        print("It's a tie!")
    elif (move == "Paper"):
        print("You lose!")
    elif (move == "Scissors"):
        print("You win!")
elif (x == "PAPER" or x == "Paper" or x =="paper"):
    print("Rock, Paper, Scissors and shoot!!")
    print("Your move: Paper")
    import random
    move = random.choice(["Rock", "Paper", "Scissors"]) 
    print ("Computer's move: " + move)
    print("---------------------------------")
    if (move == "Rock"):
        print("You win!")
    elif (move == "Paper"):
        print("It's a tie!")
    elif (move == "Scissors"):
        print("You lose!")
elif (x == "SCISSORS" or x == "Scissors" or x =="scissors"):
    print("Rock, Paper, Scissors and shoot!!")
    print("Your move: Scissors")
    import random
    move = random.choice(["Rock", "Paper", "Scissors"]) 
    print ("Computer's move: " + move)
    print("---------------------------------")
    if (move == "Rock"):
        print("You lose!")
    elif (move == "Paper"):
        print("You win!")
    elif (move == "Scissors"):
        print("It's a tie!")
elif (x == "GUNHAND" or x == "Gunhand" or x =="gunhand"):
    print("Rock, Paper, Scissors and shoot!!")
    print("Your move: Gunhand")
    import random
    move = random.choice(["Rock", "Paper", "Scissors"]) 
    print ("Computer's move: " + move)
    print("---------------------------------")
    print("You win!")
else:
    print("Whoops, that's not a valid move. Please try again!")
    quit()

print("Thank you for playing! See you again!")

