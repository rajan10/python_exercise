
from typing import Callable
# def square(x: int) -> int:
#     return x ** 2


# def my_map(fxn: Callable, numbers: list[int]) -> list[int]:
#     result = []
#     for number in numbers:
#         result.append(fxn(number))
#     return result


# print(my_map(fxn = square, numbers =[1,2,3]))


# def my_func():
#     def my_func2():
#         print("hello")
#     print("World")
    
# a=my_func
# a()

# def my_next_func( num2: int):
#     return num2 ** 2

# def my_func(num1: int):
#     result=[]
#     result.append(my_next_func(num1))
#     return result

# print(my_func(4))


# def fxn1():
#     def fxn2():
#         print("hello")
#     print("world")
    
# fxn1()


def my_function (power: int) -> Callable:
    def my_power(num: int) -> int:
        return num * power
    
    return my_power 

new_power=my_function(power=2)
print(new_power(3))