student_record = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Mike", "age": 25, "faculty":"Math"},
    4: {"_id": 4, "name": "Sita", "age": 21, "faculty":"Home Sciences"}
}


student_record2 = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Mike", "age": 25, "faculty":"Math"},  
}

def find_max(my_list: list[int])->int:    
    temp=0
    for element in my_list:
        if element>temp:
            temp=element
    return temp

def insert_one(my_collection: dict[int, dict] , value: dict[str,any])-> dict[int, dict]:
    max_key=find_max(my_collection.keys())
    my_collection[max_key+1]=value
    return my_collection


value={"_id": 4, "name": "Hari", "age": 21, "faculty":"Physics"}
result=insert_one(my_collection=student_record,value=value)
result2=insert_one(my_collection=student_record2,value=value)
print(result)
print(result2)

