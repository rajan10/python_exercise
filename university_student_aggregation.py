class Student:
    def __init__(self, name, student_id):
        self. name= name
        self. student_id= student_id
        
class University: 
    def __init__(self):
        self.students=[]
    
    def __str__(self):
        for student in self.students:
            return f"{student} is the student"
            
        
student1= Student("Ram",1001)
student2=Student("Sita",1002)

university= University()
university.students.append(student1)
university.students.append(student2)

for index, student in enumerate(university.students, start=100):
    print(f"student-{index}: {student.name}")