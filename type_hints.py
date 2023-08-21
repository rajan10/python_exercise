

student_record = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Mike", "age": 25, "faculty":"Math"},
    4: {"_id": 4, "name": "Sita", "age": 21, "faculty":"Home Sciences"}
}

def insert_many(values:list[dict]) ->dict:
    for value in values:
        key=value["_id"]
        student_record[key]=value
    return student_record
         
result_insert=insert_many([
    {"_id": 5, "name": "John", "age": 30, "faculty":"Computer"},
    {"_id": 6, "name": "Jane", "age": 25, "faculty":"Science"}
])
print(result_insert)
#create/INSERT
# def find_max(my_list):    
#     temp=0
#     for element in my_list:
#         if element>temp:
#             temp=element
#     return temp
    
# def insert_one(value):
#     max_key=find_max(student_record.keys())
#     student_record[max_key+1]=value
#     return student_record


# result=find_max()
# print(result)

# result_insert=insert_one({"_id": 4, "name": "Sita", "age": 21, "faculty":"Physics"})
# print(student_record)


#Read

# read_many()
def generic_read(query:dict):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in student_record.values():
        if value[query_key]==query_value:
            return value      

def generic_read(query: list):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    new_student_record=[value for value in student_record.values() if value[query_key]==query_value]
    return new_student_record
 

#Update
def generic_update(query: dict,data:dict) -> dict:
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in student_record.values():
        if value[query_key]==query_value:
            value.update(data)
    return student_record
    
# result_update=generic_update({"_id": 4},{"faculty":"Sital_Physics"})
# print(result_update)

#delete
##dictoanry changed size during iteration
def generic_delete(query: dict):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for key, value in student_record.items():
        if value[query_key]==query_value:
            student_record.pop(key)
          
generic_delete({"name":"Mike"})
print(student_record)
  



    

    
    
