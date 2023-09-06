from typing import Callable


def higher_order_function(fxn: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("before sum")  #check if args are int or not and for kwargs as well
        combine_list = list(args) + list(kwargs.values())
        for single_element in combine_list:
            if not isinstance(single_element, int):
                raise ValueError("All elements must be integers") # funct out of for loop
            
        output = fxn(*args, **kwargs)
        print("after sum")
        return output                    
    return wrapper

@higher_order_function
def summation(*args, **kwargs):
    sum = 0
    for i in list(args) + list(kwargs.values()):
        sum = sum+i
    return sum


try:
    new_result = summation(1, 2, 3, a=7, b=1.5)
    print(new_result)
except ValueError as e:
    print(f"Error: {e}")