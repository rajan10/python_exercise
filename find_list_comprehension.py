
"""find many by age
  find many by name
  
  use list comprehension to do the task"""

my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 25}
 }
def find_by_age(age):
    result_age_list=[value for value in my_collection.values() if value['age'] == age]
    return result_age_list

def find_by_name(name):
    result_name_list=[value for value in my_collection.values() if value['name']==name]
    return result_name_list
 
result_name_list=find_by_name("Jane")   
print(result_name_list)      
result_age_list=find_by_age(25)
print(result_age_list)