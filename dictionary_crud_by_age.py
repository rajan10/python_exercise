# my_collection = {
#     1: {"_id": 1, "name": "John", "age": 30},
#     2: {"_id": 2, "name": "Jane", "age": 25},
#     3: {"_id": 3, "name": "Mike", "age": 35}
# }
# # [{"_id": 4, "name": "Sita", "age": 40},{"_id": 5, "name": "Gita", "age": 41}]
 
# def max_key(dict_collection):
#     temp=0
#     for key in dict_collection.keys():
#         if key > temp:
#             temp=key
#     return temp

# def insert_one(my_dict):
#     new_key=max_key(my_collection)+1
#     my_collection[new_key]=my_dict
#     return my_collection
 
# def insert_many(my_list):
#     for my_dict in my_list:
#         new_key=max_key(my_collection)+1
#         my_collection[new_key]=my_dict
#     return my_collection 

# """create a function find_one_by_name   which will take name as argument and return respective dict with 
# the given name"""


# new_collection= insert_many([{"_id": 4, "name": "Sita", "age": 40},{"_id": 5, "name": "Mita", "age": 42}])
# print(new_collection)
 
 
my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 35}
 }
    # my_collection[name] ="Sita"

# {"_id": 4, "name": "Sita", "age": 40}
"""find one by age """


def find_one_by_age(age):
    for k,v in my_collection.items():
        if v["age"]==age:
            return v
            break
    return {}
        
    
    
result=find_one_by_age(305)
print(result)