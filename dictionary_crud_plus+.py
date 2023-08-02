
my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 35}
 }
    # my_collection[name] ="Sita"
def find_one_by_name(name):
    for k,v in my_collection.items():
        # for k1,v1 in v.items():
        if v["name"]==name:
            return v  
    return {}
                 
result=find_one_by_name("Jane")
print(result)
