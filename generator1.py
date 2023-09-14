# Creating an iterable (list)
my_list = [1, 2, 3, 4, 5]

# Creating an iterator from the iterable
my_iterator = iter(my_list)

# Using the `next` function to manually get items from the iterator
try:
    while True:
        item = next(my_iterator)
        print(item)
except StopIteration:
    pass

new_list = [element for element in range(5)]

generator_obj =(element*2 for element in new_list)
print(generator_obj)
for i in generator_obj:
    print(i)