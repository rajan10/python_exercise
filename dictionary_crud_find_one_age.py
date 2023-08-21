
"""find one by age """

my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 25}
 }
def find_one_by_age(age):
    for value in my_collection.values():
        if value["age"]==age:
            return value
         
    return {}
            
result=find_one_by_age(25)
print(result)