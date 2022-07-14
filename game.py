# this is the "game.py" file...

# import modules
import random

# Welcome message
print (" ")
print("Welcome to Rock, Paper, Scissors!")

#Prompt user input
x = input("Choose your move from either Rock, Paper or Scissors: ")
print("---------------------------------")

if (x == "ROCK" or x == "Rock" or x =="rock"):
    print("Rock, Paper, Scissors and shoot!!")
    print("Your move: Rock")
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
    move = random.choice(["Rock", "Paper", "Scissors"]) 
    print ("Computer's move: " + move)
    print("---------------------------------")
    print("You win!")
else:
    print("Whoops, that's not a valid move. Please try again!")
    print (" ")
    quit()

print("Thank you for playing! See you again!")
print(" ")
