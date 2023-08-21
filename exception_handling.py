

# try:
#     num=input("Enter number")
#     result=num/0
#     print("REsult:",result)
#     print("hellloo")
# except ValueError
# except Exception as e:  
#    print(f"There is error and the error name is '{e}'")

    
# # except ZeroDivisionError:12
#     # print(".........Cannot divide by zero")


while True:
    try:
        x=int(input("Please enter a number:"))
        break
    except ValueError:
        print("OOps! that was no valid number. Try again...")
        
    finally:
        print("I'm 'finally'done now")