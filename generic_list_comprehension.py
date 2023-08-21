
"""find many by age
  find many by name
  
  use list comprehension to do the task"""
  
""" 
def find(query):
    return []
    

query1={"name": "John"}
query2={"age": 25}
query3={"_id": 1}
    """

my_collection = {
    1: {"_id": 1, "name": "John", "age": 30},
    2: {"_id": 2, "name": "Jane", "age": 25},
    3: {"_id": 3, "name": "Mike", "age": 25}
 }

def find(query):
    matching_values=[]
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    result=[ value for value in my_collection.values() if value[query_key]==query_value]  
    return result
        
            
result_age=find({"age": 25})
print(result_age)
result_name=find({"name": "Mike"})
print(result_name)