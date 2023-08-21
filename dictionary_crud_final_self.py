student_record = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Sita", "age": 25, "faculty":"Math"},
    4: {"_id": 4, "name": "Sita", "age": 21, "faculty":"Home Sciences"}
}
#use  max_key() and implement
def insert_many(values:dict)->list:
    for value in values:
        key=value["_id"]
        student_record[key]=value
    return student_record       

# create/INSERT
def find_max(my_list:list)->int:    
    temp=0
    for element in my_list:
        if element>temp:
            temp=element
    return temp

def insert_many(values:dict, my_collection: dict)->dict:
    max_key=find_max(my_collection.keys())
    for value in values:
        my_collection[max_key+1]=value  
    return my_collection   
values= [{"_id": 5, "name": "John1", "age": 38, "faculty":"Computer1"},{"_id": 6, "name": "Jane1", "age": 24, "faculty":"Science1"}]

result_insert_many=insert_many(values,my_collection=student_record)
print(result_insert_many)       
         
def insert_one(value:dict,my_collection:dict)->dict:
    max_key=find_max(student_record.keys())
    student_record[max_key+1]=value
    return student_record

result_insert=insert_one({"_id": 10, "name": "Sohn", "age": 11, "faculty":"Computer"},my_collection=student_record)
print(result_insert)

#Read

# read_many()
def generic_read(query: dict,my_collection: dict):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in my_collection.values():
        if value[query_key]==query_value:
            return value
              
# return always goes out of function
 
#using list comprehension
def generic_read(query: dict,my_collection:dict):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    new_my_collection=[value for value in my_collection.values() if value[query_key]==query_value]
    return new_my_collection
 
result_read=generic_read({"_id": 3}, my_collection=student_record)   
print(result_read)
    
#Update
def generic_update(query:dict,data: dict,my_collection:dict)->dict:
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in my_collection.values():
        if value[query_key]==query_value:
            value.update(data)
    return my_collection
    
result_update=generic_update({"_id": 4},{"faculty":"Sitalll_Physics1"},my_collection=student_record)
print(result_update)

#delete
#delete_many to do using keys to be deleted in list
def generic_delete(query:dict,my_collection:dict)->dict:
    keys_to_be_deleted=[]
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for key, value in my_collection.items():
        if value[query_key]==query_value:
            keys_to_be_deleted.append(key)
            # del student_record[key]
    for key in keys_to_be_deleted:
        del my_collection[key]
                              
   #pop() dictionary built-in methods
    
generic_delete({"name":"Sita"},my_collection=student_record)
print(student_record)



    

    
    
