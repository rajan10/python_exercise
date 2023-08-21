
from random import random,choice
from game_constants import options
import sys

def check(user_input, computer_input):
        if(user_input==computer_input):
            print("Stalemate, pls. play again!")     
        elif(user_input=="rock" and computer_input=="scissors") or (user_input=="scissors" and computer_input=="paper")or (user_input=="paper" and computer_input=="rock"):
            print("Congratulation! you win!")    
        else:  
            print("Computer wins!")    
           
def play_game():
    while True:    
        print("Lets play Rock, Paper and Scissor Game")
        user_input=input("\nPlease enter any one (Rock, Paper, Scissors, or 'quit' to exit):").strip()
        if user_input == "quit":
            print("Thanks for playing")
            break 
        elif user_input in options:
            computer_input=choice(options)
            print("Computer's choice:",computer_input)
            check(user_input.lower(), computer_input.lower())          
        else:
            print("Invalid input. Please enter Scissors, Paper, Rock or 'quit'.")
        if not play_again():  #function gets call first and returns and that return value is evaluated with conditional stament
            break      
    
def play_again():
    print("Do you want to play again. Enter(Yes/No)")
    user_input=input().lower()   #when there are 2 or more functions called together with '.' operator, function call executes from left to right
    if user_input=="yes":
        return True
        
    elif (user_input=="no"):
        print("Thank you for playing")
        return False
        
    else:
        print("Invalid input.Please enter 'yes' or 'no'")
        return True
                

#  create a class named game_controller
#  Add all the functions to that class
#  add options as class variables 
#  delete 'game_constants.py'
 
#  in main.py, instantiate from game_controller and call play_game function
 
#  while true in roll_dice, roll again? yes continue loop else break

 
    


            


