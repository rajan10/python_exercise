student_record = {
    1: {"_id": 1, "name": "John", "age": 30, "faculty":"Computer"},
    2: {"_id": 2, "name": "Jane", "age": 25, "faculty":"Science"},
    3: {"_id": 3, "name": "Mike", "age": 25, "faculty":"Math"}
}
#update_one 
def update_one(query, data):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in student_record.values():
        if value[query_key]==query_value:
            value.update(data)
            break
 
# update_one({"age":25},{"faculty":"Physics"})
# print(student_record)

#update_many
def update_many(query, data):
    query_key=list(query.keys())[0]
    query_value=list(query.values())[0]
    for value in student_record.values():
        if value[query_key]==query_value:
            value.update(data)
          
 
update_many({"age":25},{"faculty":"Physics"})
print(student_record)