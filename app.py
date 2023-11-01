#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

#write 'hello world' to console
print("Hello World!")

#Define the game elements Rock, Paper, Scissors as a list
game_elements = ["Rock", "Paper", "Scissors"]

#Define function to get user's choice
def get_user_choice():
    user_choice = input("Enter Rock, Paper, or Scissors: ")
    return user_choice

#Define function to get computer's choice   
def get_computer_choice():
    import random
    computer_choice = random.choice(game_elements)
    return computer_choice

#Define function to determine winner
def determine_winner(user_choice, computer_choice): 
#If user and computer make the same choice, it's a tie 
    if user_choice == computer_choice:
        return "It's a tie!"    
    #If user chooses Rock and computer chooses Scissors, user wins 
    elif user_choice == "Rock" and computer_choice == "Scissors":
        return "You win!"
    # If user chooses Paper and computer chooses Rock, user wins
    elif user_choice == "Paper" and computer_choice == "Rock":
        return "You win!"
    # If user chooses Scissors and computer chooses Paper, user wins
    elif user_choice == "Scissors" and computer_choice == "Paper":
        return "You win!"
    # If user chooses Rock and computer chooses Paper, computer wins    
    elif user_choice == "Rock" and computer_choice == "Paper":
        return "Computer wins!"
    # If user chooses Paper and computer chooses Scissors, computer wins
    elif user_choice == "Paper" and computer_choice == "Scissors":
        return "Computer wins!"
    # If user chooses Scissors and computer chooses Rock, computer wins
    elif user_choice == "Scissors" and computer_choice == "Rock":
        return "Computer wins!"
    # If user enters invalid choice, return error message   
    else:
        return "Invalid input. You must enter Rock, Paper, or Scissors."    
    #Define main function to run the game

def play_game():    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose: " + user_choice)
    print("The computer chose: " + computer_choice)
    print(determine_winner(user_choice, computer_choice))
         
#Run the game 
play_game()

#Add variable to display game in browser
@app.route("/game")
def game():
    return play_game()



@app.route("/")
def hello():
    return app.send_static_file("index.html")
