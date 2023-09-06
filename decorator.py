
from typing import Callable


def higher_order_function(fxn: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("before sum")  #check if args are int or not and for kwargs as well
        output = fxn(*args, **kwargs)
        print("After sum")
        return output
                    
    return wrapper

@higher_order_function
#existing function being decorated by @higher_order_function
def summation(*args, **kwargs):
    sum = 0
    for i in list(args) + list(kwargs.values()):
        sum = sum+i
    return sum


# calling existing function
new_result = summation(1, 2, 3, a=3.4, b=6)
print(new_result)
