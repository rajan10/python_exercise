from functools import reduce

# # a= [1,2,3]
# # def square(a: list-> list:)

# from functools import reduce

# # kg ->gram


# # map(function that works at iterator level, iterable)

# list_of_kg = [1, 2, 3, 4]

# result = map(lambda x: x * 1000, list_of_kg)

# new_result = []
# for i in result:
#     new_result.append(str(i) + " grams")

# # for i in new_result:
# #     print(i)

# new_format = zip(list_of_kg, new_result)
# print(next(new_format))  # zip outputs tuple eg (1,1000)

# # for i, j in new_format:
# #     print(i, j)


# # print(new_format)
# # tuple element (1,10000)
# # print(next(new_format))

# for i, j in new_format:
#     result = f"{i} Kg is equal to {j}"
#     # print(result)

#     # 1 Kg is equal to 1000gram

# # print(new_format)

# # print(new_result)


# # using reduce funct find the factorial

# # Print("Enter a number to ")

# number_list = [1, 2, 3, 4, 5]

# result = reduce(lambda x, y: x if x > y else y, number_list)
# #reduce funct takes 2 first 2 items from the iterable and applies.
# #it takes the result to x and takes another argument at y. This process
# # continues until there is no more items
# print(result)


# nums = [1, 2, 3, 4]
# ans = reduce(lambda x, y: x + y, nums)
# print(ans)

# using reduce function to find the factorial of input number


# number = input("Enter number to find the factorial: ")
# 4 =12X2X1  =24


# new_list =[4,3,2,1]
# 12
# x=12, y=2
# x=24, y=1
# x=24


# def factiorial_func(n: int) -> int:
#     factorial = reduce(lambda x, y: x * y, range(1, n + 1))
#     return factorial


# print(factiorial_func(3))
# print(factiorial_func(4))
# print(factiorial_func(5))


# print(is_even(30))

from typing import Callable

# # my_list=range(1,11)
# # my_list = [1, 2, 3, 4]
# # my_list = [2, 4]


# def is_even(n: int):
#     # return True if n % 2 == 0 else False
#     return bool(n % 2 == 0)


# def filter_func(fxn: Callable, my_list: list[int]) -> list[int]:
#     even_list = []
#     for i in my_list:
#         if fxn(i):
#             even_list.append(i)
#     return even_list


# result = filter_func(is_even, range(1, 11))
# print(result)


def is_even(n: int):
    # return True if n % 2 == 0 else False
    return n % 2 == 0  # comparison operator return True or False


# '''User define filter()'''

# def filter_func(fxn: Callable, my_list: list[int]) -> list[int]:
#     even_list = []
#     for i in my_list:
#         if fxn(i):
#             even_list.append(i)
#     return even_list

# ''' Python built-in filter() '''
# result = filter(lambda x: x % 2 == 0, range(1, 11))
# print(list(result))

# contact_list similar to cell , persistence in dict, file_handling

# project 1
# add contact to list
# search the contact/ filter by NameError
# view all contact list


# project 2 to do list, show , create , delete, persistence on me
# console list
