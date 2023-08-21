
"""find many by age
  find many by name
  
  use list comprehension to do the task"""

my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 25}
 }
def find_by_age(age):
    matching_values=[]
    for value in my_collection.values():
        if value["age"]==age:
           matching_values.append(value)   
    return matching_values

def find_by_name(name):
    matching_values=[]
    for value in my_collection.values():
        if value["name"]==name:
           matching_values.append(value)
    return matching_values      
            
result=find_by_name("Sita")
print(result)