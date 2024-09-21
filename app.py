import random

choices = ["rock","paper","scissore"]

computer = random.choice(choices)

player = None

while player not in choices:
    player= input("rock,paper,scissore?: ").lower()

if computer == player:
    print("Computer: ",computer)
    print("Player: ",player)
    print("Tie!")
elif player == "rock":
    if computer == "paper":
         print("Computer: ",computer)
         print("Player: ",player)
         print("You lose!")
    if computer == "scissore":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You win!")
elif player == "scissore":
    if computer == "rock":
         print("Computer: ",computer)
         print("Player: ",player)
         print("You lose!")
    if computer == "paper":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You win!")
elif player == "paper":
    if computer == "scissore":
         print("Computer: ",computer)
         print("Player: ",player)
         print("You lose!")
    if computer == "rock":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You win!")