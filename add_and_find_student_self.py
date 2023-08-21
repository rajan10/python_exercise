
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

#CREATE
def create_student(_id,name,faculty:object)->list:
    new_student=Student(_id,name,faculty)
    student_list.append(new_student)
    return student_list

# result_create_student=create_student(40,"Ganesh","Humanities")
# for student in result_create_student:
#     print(student)

#READ
def read_students()->Student:
    for student in student_list:
        print(f"ID: {student._id}\nName: {student.name}\nFaculty: {student.faculty}")
        print("=" *25)
        
# read_students()   

#UPDATE
def update_student_by_id(_id:int, values:dict)->str:
    for student in student_list:
        if student._id==_id:
            student.name=values["name"]
            student.faculty=values["faculty"]
            return f"Student with id {_id} updated Successfully"
            

# print(update_student_by_id(1, {"name":"Ganapati","faculty":"NLP"}))
# print("Below is the updated list")
# read_students()
  
#DELETE
def delete_student_by_id(_id:int)->str:
    for student in student_list:
        if student._id==_id:
            student_list.remove(student)
            return f"Student with ID: {_id} deleted successfully!"
    
print(delete_student_by_id(1))
print("Student list after deletion")
read_students()


     
     




            