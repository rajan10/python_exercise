
from random import random,choice
from game_constants import options

def play_game():
    print("Lets play Rock, Paper and Scissor Game")
    user_input=input("\nPlease enter any one (Rock, Paper, Scissors):")
    print("\nhello")
    computer_input=choice(options)
    print("Computer input:",computer_input)


    def check(user_input, computer_input):
        if(user_input==computer_input=="Rock") or (user_input==computer_input=="Scissors") or (user_input==computer_input=="Paper"):
            print("Stalemate, pls play again!")
            
        elif(user_input=="Rock" and computer_input=="Scissors") or (user_input=="Scissors" and computer_input=="Paper")or (user_input=="Paper" and computer_input=="Rock"):
            print("you win!")
            
        else:
            (user_input=="Scissors" and computer_input=="Rock") or (user_input=="Paper" and computer_input=="Scissors")or (user_input=="Rock" and computer_input=="Paper")
            print("Computer win")
    check(user_input, computer_input)
    
def play_again():
    print("Do you want to play again. Enter(Yes/No)")
    user_input=input("").lower()
    if user_input=="yes":
        play_game()
        
    elif (user_input=="no"):
        print("Thank you for playing")
    
    else:
        print("Please enter yes or no")
            

 
    


            


