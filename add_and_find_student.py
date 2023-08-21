"""
   list of Student objects [student1: object1
    student2:object2]
    
    def add_student():
        
    def generic_find_student():
        
    def generic_update_student():
    
    def generic_delete_student():
        
        class, conditional, datatype
        
        api ->framework 
    
    """  
class Student:
    def __init__(self,_id, name, faculty) -> None:
        self._id=_id
        self.name=name
        self.faculty=faculty
    
    def __str__(self):
        return f"ID: {self._id} \n Name: {self.name} \n Faculty:{self.faculty}"
        
student1= Student(1,"Ram","computer")
student2= Student(2,"Sita","Home Science")
student3= Student(3,"Laxman","AI")
student4= Student(4,"Bharat","Data Science")
student_list=[student1,student2, student3, student4]

# create/add
def add_student(student: Student)->list:
    student_list.append(student)
    return student_list

# find/read
def find_student_by_id(query_value: int)->Student:
    for student in student_list:
        if query_value==student._id:
            return student
 #update       
def generic_update_student(_id: int, new_name: str, new_faculty: str)->Student:
    for student in student_list:
        if student._id==_id:
            student.name=new_name
            student.faculty=new_faculty
            return student
#delete       
def delete_student(_id: int):
    for student in student_list:
        if student._id== _id:
            student_list.remove(student) 
            
print(len(student_list)) 
delete_student(4)    
print(len(student_list)) 
    
# result_update_student=generic_update_student(4,"Hari","Account") 
# print(result_update_student)

# student5=Student( 5, "Rajan", "Art" )               
# result_add_student=add_student(student5) 
# print(result_add_student)

   
# for student in student_list:
#      print(f"ID: {student._id}, Name: {student.name}, Faculty:{student.faculty}") 

# result_find_student=find_student_by_id() 
# read_student(result_find_student)
    

     
     




            