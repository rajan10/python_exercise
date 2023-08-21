import random

print("Dice game!")

roll_count = 0  # Initialize the loop counter

while True:
    user_input = input("Do you want to roll the dice? (Yes/No) ").lower()

    if user_input == "yes":
        roll_dice = random.randint(1, 6)
        roll_count += 1  # Increment the roll counter
        print(f"\nYou rolled {roll_dice}!")

        user_input = input("Do you want to roll the dice again? (Yes/No) ").lower()
        if user_input == "yes":
            print(f"This is your {ordinal(roll_count + 1)} time playing the Dice game.")  # Using ordinal() to get 1st, 2nd, 3rd, etc.
            roll_dice = random.randint(1, 6)
            print(f"\nYou rolled {roll_dice}!")
        elif user_input == "no":
            break
        else:
            print("Invalid option, please type 'Yes' or 'No'")
    elif user_input == "no":
        break
    else:
        print("Invalid option, please type 'Yes' or 'No'")
