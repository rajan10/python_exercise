my_dic_tuple_as_keys ={("Raj", 40):"Developer", ("Saj", 25):"IT support",("Sita", 35):"HouseWife"}
print(my_dic_tuple_as_keys)

my_set={"hello", "how", "are", "you"}
print(my_set)
print(id(my_set))

my_set.add("good")
print(my_set)
print(id(my_set))

my_frozen_set= frozenset(my_set)
print(my_frozen_set)
#my_frozen_set.add("Rajan")
#print(my_frozen_set)

print(dir(frozenset))

print("=================")
x=["apple", "banana"]
y=["apple", "banana"]
if (x is y):
    print("True")
print("false")
if (x==y):
    print("contents of x and y is same and hence returns True")
else:
    print("contents are not same and hence doesnot not return false")
    
print("++++++++++++++++++++++++++++++")   
print("test string is immutable")

my_string="immutable"
print(type(my_string))
print(id(my_string))
print("After trying to add")
my_string+="add this"
print(type(my_string))
print(id(my_string))

print("list to test for mutability, it will have same memory address")
my_list=["hello",True,123.45]
print(type(my_list))
print(id(my_list))
print("after inserting one more elements in the list")
my_list.insert(1,False)
print(type(my_list))
print(id(my_list))


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Driver:
    def __init__(self, name):
        self.name = name

driver1 = Driver("John")
car1 = Car("Toyota", "Camry")
car1.driver = driver1  