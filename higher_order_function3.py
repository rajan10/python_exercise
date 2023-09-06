
from typing import Callable


# def processing():
#     sleep(4)
#     print("I'm doing some processing")


# def print_time_diff(fxn, Callable)-> Callable:
#     def wrapper():
#         start_time=time()
#         fxn()
#         end_time=time()
#         print(f"Time to process: {end_time-start_time}")
#     return wrapper

# print_time=print_time_diff(processing)
# print_time()


import time


def processing(delay: int):
    time.sleep(delay)
    print("I'm doing some processing")


def print_time_diff(fxn: Callable) -> Callable:  # this function is changing the above function  
    def wrapper(delay):
        start_time = time.time()
        fxn(delay)
        end_time = time.time()
        print(f"Time to process: {end_time - start_time}")
    return wrapper


print_time = print_time_diff(processing)
print_time(2)  # Call the print_time function to see the time difference.






