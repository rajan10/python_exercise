
from typing import Callable
import time

def add(*args, **kwargs):
    sum=0
    for arg in list(args)+ list(kwargs.values()):
        sum=sum+arg
    return sum

def my_function(fxn: Callable)-> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fxn(*args, **kwargs)
        end_time = time.time()
        print(f"The start time and end time is {end_time-start_time}")
        return result
    return wrapper


print_this = my_function(add)
result = print_this(10, 20, 30, a=4, b=4)
print(result)