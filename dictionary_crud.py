""" create a function name insert_one that will take a dict as argument that will append that 
argument in my_collection dictionary
key of the my_collection dictionary will be increamented by +1 in every addition of new dictionary values
"""

my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 35}
}

def maximum_key(my_dict):
    for key in my_dict.keys():
        temp=0
        if key>temp:
            temp=key
    return temp

def insert_one(my_dict):
    new_key=maximum_key(my_collection)+1
    my_collection[new_key]=my_dict

insert_one({"_id": 4, "name": "Sita", "age": 40})  
insert_one({"_id": 5, "name": "Gita", "age": 41})
print(my_collection) 
