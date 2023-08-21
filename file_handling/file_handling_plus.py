from file_handling_controller import read_student_by_roll,write_student,update_student_by_id,get_all_students
import sys
# print(
#     """
#         1. Read Student.
#         2. Add student.
#         3. Show all the Students.
#         4. Quit
#         Type numbers (1,2,3) to select option.
#     """
#     )
# "Student Information Name, Roll etc"
def menu_display():
        while True:    
            print("""==== Welcome to Student Info Menu ====
        1. Read Student by Roll
        2. Add Student
        3. Update Student
        4. Show all the Students
        5. Quit
==== Welcome to Student Info Menu ====
              """)
            user_choice=int(input("Please type numbers (1,2,3,4) to select option:"))
            if user_choice == 1:
                print("You chose 1")
                search_roll=input("Enter the Roll Number that you want to read:")
                student_info=read_student_by_roll(search_roll)
                if student_info:
                    print("Student Info:")
                    print(student_info)
                else:
                    print(f"Student with roll number {search_roll} not found!")
                   
            elif user_choice == 2:   
                print("You chose  2") 
                write_student()
                
            elif user_choice == 3:  
                print("You chose  3")
                search_roll=input("Enter the Roll to update:")
                updated_student_list=update_student_by_id(search_roll)
             
   
            elif user_choice == 4:  
                print("You chose  4")
                students_info_list=get_all_students()
                print("All Students Information Record")
                print('=' *35)  
                for info in students_info_list:
                    print(info.strip())
                print("=" * 35)
                
            elif user_choice == 5:  
                print("You chose  5")
                print("Thank you for using Student Info Menu")
                sys.exit()
        
            else:
                print("Invalid choice. Please 1, 2, 3 and 4 or 'quit'.")
                break    


