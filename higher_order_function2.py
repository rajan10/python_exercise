from typing import Callable
from time import time


# def print_hello(): # the behavior of this function will be modified
#     print("hello")


# def time_difference(fxn: Callable):   # modifier function
#     def function_being_modified():      # wrapper function the function being tweaked
#         start_time = time()
#         fxn()
#         end_time = time()
#         print(f"The start time and end time of execution is: {start_time} and { end_time}")
#     return function_being_modified


# same_wrapper_function = time_difference(print_hello)
# same_wrapper_function()


# def function_being_modified(t: str):
#     print("helllo")


# def time_difference(fxn: Callable)-> Callable:
#     def function_being_modified():
#         start_time = time(t)
#         fxn(t)
#         end_time = time()
#         print(f"The start time and end time of execution is: {start_time} and {end_time}")
#     return function_being_modified

   
# new_function_being_modified=time_difference("hello")
# print(new_function_being_modified)



def apply(funx: Callable, x: int) -> Callable:
    return funx(x)

def square(x: int):
    return x ** 2

result =apply(square, 2)
print(result)


# from typing import Callable

# def apply(funx: Callable, x: int) -> int:
#     return funx(x)

# def square(x: int) -> int:
#     return x ** 2

# result = apply(square, 2)
# print(result)


