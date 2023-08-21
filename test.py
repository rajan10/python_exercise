# # # # for i in range(1,10,2):
# # # #     print(i)
    
    
# # # # def string_to_dicti(string):
# # # #     char_dict={}
# # # #     for char in string:
# # # #         if char not in char_dict.keys():
# # # #             char_dict[char]=1
# # # #         else:
# # # #             char_dict[char]=char_dict[char]+1
# # # #     return char_dict      

# # # # print(string_to_dicti("hello"))


# # # # my_list={"Rajan",30, "NY"}
# # # # for k,v in enumerate(my_list, start=-1):
# # # # 	print(f" Student {k}: {v}")
 
 
# # # # x="awesome"
# # # # def my_func():
# # # #     global x
# # # #     x="fantastic"
# # # #     return x    
# # # # print(my_func())

# # student_record = {
# #     10: {"_id": 100, "name": "John", "age": 30},
# #     20: {"_id": 200, "name": "Jane", "age": 25},
# #     30: {"_id": 300, "name": "Mike", "age": 25}
# #  }
# # # # def find(query):
# # # #     matching_values=[]
# # # #     query_key=list(query.keys())[0]
# # # #     query_value=list(query.values())[0]
# # # #     for value in student_record.values():
# # # #         if value[query_key]==query_value:
# # # #             matching_values.append(value)
                    
# # # #     return matching_values


# # # # result_age=find({"age":30}) 
# # # # result_name=find({"name":"Mike"}) 
# # # # print(result_age)  
# # # # print(result_name) 
    
# # # def delete_many(age):
# # #   new_student_record=list(filter(lambda item: item[1]["age"]!=age,student_record.items()))
# # #   return  new_student_record

# # # result_delete=delete_many(25)
# # # print(result_delete)

# # # #using lambda function to add
# # # add =lambda x,y:x+y

# # # result=add(1,2)
# # # print(result)

# # # #using lambda function with map()
# # # numbers=[1,2,3,4]
# # # double_numbers= list(map(lambda x: x*2, numbers))
# # # print(double_numbers)

# # # #using lambda with sorted()
# # # students =[("Rajan",25), ("Shyam",28), ("Rita",5)]
# # # sorted_by_age=sorted(students,key=lambda x:x[1])
# # # print(sorted_by_age)

# # def generic_read(query):
# #     query_key = list(query.keys())[0]
# #     query_value = list(query.values())[0]
# #     new_student_record = [student_record[key] for key in student_record if student_record[key][query_key] == query_value]
# #     return new_student_record

# # result_read = generic_read({"_id": 200})
# # print(result_read)

# class Car:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#         self.driver=None
# class Driver:
#     def __init__(self, name):
#         self.name=name
        
# Rajan= Driver("Raj")
# Toyota= Car("Toytota","Camry")
# Toyota.driver  = Rajan

# if Toyota.driver is not None:
#     print(f"The car {Toyota.make} {Toyota.model} is driven by {Rajan.name}")
# else:
#     print(f"NO driver assigned")
    
    
# class Book:
#     def __init__(self,title, author):
#         self.title = title
#         self. author= author
# class Borrower:
#     def __init__(self,name):
#         self.name=name
        
# book1=Book("The Catcher in the Rye","Salinger")
# borrower1=Borrower("Rajan Gauchan")

# book1.borrower =borrower1 # dynamically creating object attribute; this is possible in Python
# print(f" The '{book1.title}' is borrowed by '{borrower1.name}'")

# class Vehicle:
#     def __init__(self,make, model):
#         self.make=make
#         self.model=model
# class Car(Vehicle):
#     def __init__(self, make, model,num_doors):
#         super().__init__(self,make, model)
#         self.num_doors=num_doors
# car1=Car("Toyota", "Camry", 4)
# print(car1.make)
# print(car1.num_doors)
#mutable objects/ changeable
# My_list=[1,2,3]
# b=My_list

# b[0]=100
# print(b)
# print(My_list)

# #immutable
# x=10
# y=x
# y=500
# print(x)
# print(y)


# def ordinal(n):
#     if 10 <= n % 100 <= 20:
#         suffix = 'th'
#     else:
#         suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
#     return f"{n}{suffix}"

# ord=ordinal(21)
# print(ord)


# def print_num(n):
#     for each in range(1,n):
#         yield each
# data= print_num(100)
# print(next(data))
# print(next(data))
# print(next(data))

# for num in print_num(100):
#     print(num)


# while True:
#     try:
#         print(next(data))
#     except:
#         break

# # w+ => writing and then reading it won't overwrite existing data
# f=open('student.txt', mode='w+')
# print(f.tell()) #0
# f.write('youtube') #writes 'youtube' =cursor is at 7
# print(f.tell())  #7
# f.write("hello")  #writes 'hello' from cursor 7 it writes 'hello', cursor is at 12
# print(f.tell()) #12
# f.seek(0) #brings cursor to beginning of the page.
# print(f.read())  #prints youtubehello but if f.seek(0) is not written then it will not print anything coz at position 12
# # there is no data to read


f=open('student_write.txt', mode='w+')
f.write('write')
f.write('write1')
f.write('write2')
print(f.tell())

print(f.read())
       