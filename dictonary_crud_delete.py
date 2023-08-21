""" 2delete_many

 task2: generic_delete_one name, age, _id (query)
 
 task3:generic_delete_many
  """

student_record = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Mike", "age": 25, "faculty":"Math"}
}

def delete_one(name):
    for key, value in student_record.items():
        if value["name"]==name:
            student_record.pop(key)
            break
        
def delete_one(age):
    for key,value in student_record.items():
        if value["age"]==age:
            student_record.pop(key)
            break

def delete_many(age):
    new_student_record={}
    for key,value in student_record.items():
        if value["age"]!= age:
            new_student_record[key]=value
    return new_student_record
        
def generic_delete_many(query):  
    new_student_record={}
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for key, value in student_record.items():
        if value[query_key]!=query_value:
            new_student_record[key]=value
    
    return new_student_record
            
            
    


# delete_result=generic_delete_many({"name": "John"})
# print(delete_result)

delete_result=generic_delete_many({"faculty": "Computer"})
print(delete_result)
  
  
                    


# delete_one("John")
# print(student_record)

# delete_one(25)
# print(student_record)

# delete_result=delete_many(25)
# print(delete_result)
