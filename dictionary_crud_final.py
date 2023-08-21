student_record = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Sita", "age": 25, "faculty":"Math"},
    4: {"_id": 4, "name": "Sita", "age": 21, "faculty":"Home Sciences"}
}
#use  max_key() and implement
def insert_many(values):
    for value in values:
        key=value["_id"]
        student_record[key]=value
    return student_record
         
# result_insert=insert_many([
#     {"_id": 5, "name": "John", "age": 30, "faculty":"Computer"},
#     {"_id": 6, "name": "Jane", "age": 25, "faculty":"Science"}
# ])
# print(result_insert)
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
def generic_read(query):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in student_record.values():
        if value[query_key]==query_value:
            return value
        
        
# return always goes out of function
 
 #using list comprehension
def generic_read(query):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    new_student_record=[value for value in student_record.values() if value[query_key]==query_value]
    return new_student_record
 
# result_read=generic_read({"_id": 3})   
# print(result_read)
    

#Update
def generic_update(query,data):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in student_record.values():
        if value[query_key]==query_value:
            value.update(data)
    return student_record
    
# result_update=generic_update({"_id": 4},{"faculty":"Sital_Physics"})
# print(result_update)

#delete
#delete_many to do using keys to be deleted in list
def generic_delete(query):
    keys_to_be_deleted=[]
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for key, value in student_record.items():
        if value[query_key]==query_value:
            keys_to_be_deleted.append(key)
            # del student_record[key]
    for key in keys_to_be_deleted:
        del student_record[key]
                              
   #pop() dictionary built-in methods
   
   #using dict comprehension
#    query_key=list(query.keys())[0]
#    query_value=list(query.values())[0]
#    new_student_record={key :value for key,value in student_record.items() if value[query_key]!=query_value }    
generic_delete({"name":"Sita"})
print(student_record)



    

    
    
