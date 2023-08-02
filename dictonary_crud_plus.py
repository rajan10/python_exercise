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
"""
 create function with a name insert_many that will take list of dict as an argument and append 
 all dictionary from the list to my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 35}
 key of my_collection dictionary will be increased by 1 in every addition of value
 
 input = inset_many([{"_id": 4, "name": "Sita", "age": 40},{"_id": 5, "name": "Gita", "age": 50},...]
"""
def insert_one(my_dict):
    new_key=maximum_key(my_collection)+1
    my_collection[new_key]=my_dict
    
def insert_many(my_list):
    for my_dict in my_list:
        insert_one(my_dict=my_dict)

insert_many([{"_id": 4, "name": "Sita", "age": 40},{"_id": 5, "name": "Gita", "age": 50}])
print(my_collection)
