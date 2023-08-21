
student_record = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Mike", "age": 25, "faculty":"Math"}
}

def delete_one(age):
    new_student_record={key:value for key,value in student_record.items() if value["age"]!=age}
    return new_student_record


def generic_delete(query):
    new_student_record={}
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    new_student_record={key:value for key,value in student_record.items() if value[query_key]!=query_value}
    return new_student_record
    

# delete_result=delete_one(25)
# print(delete_result)
   
generic_delete_result=generic_delete({"age": 25})
print(generic_delete_result)
    
    