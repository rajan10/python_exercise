import random

#  while true in roll_dice, roll again? yes continue loop else break
print("Dice game!")
while True:
   
    user_input=input("Do you want to roll the dice?(Yes/No) ").lower()
    if user_input=="yes":
        roll_dice=random.randint(1,6)
        print(f"\nYou rolled {roll_dice}!")
        
    elif user_input=="no":
        print("Thank you for playing! Good bye!")
        break  
        
    else:
        print("Invalid option, pls type 'Yes' or 'no'")


# # Do play again()

# # random is a module and choice is a built-in function in it
# fruits=["apple","banana","cherry"]
# pesuedo_random=random.choice(fruits)
# print(pesuedo_random)

# # fruits=["apples","bananas","cherrys"]
# # shuffle_elements=random.shuffle(fruits)
# # print(shuffle_elements)

# numbers = ["1", 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Shuffling the list of numbers
# random.shuffle(numbers)

# # Print the shuffled list
# print(numbers)



# random_float = random.uniform(2.5, 5.5)
# print(random_float)

# random.random() 
# print(random.random() )