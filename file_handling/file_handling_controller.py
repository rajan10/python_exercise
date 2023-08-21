import sys

def read_student_by_roll(roll_number):
    try:
        with open("file_handling\student_info.txt","r") as file_object:
            for line in file_object:
                if roll_number in line:
                    return line
      
    except FileNotFoundError:
        print("File not Found")
        
def write_student():  
    with open("file_handling\student_info.txt", "a") as file_object:
        print("Existing File opened for adding Student Record successfully")
        while True:
            student_roll=input("Enter student roll no:")
            student_name=input("Enter student name:")
            student_faculty=input("Enter student faculty:")
            content=f"Roll:{student_roll}\tName:{student_name}\tFaculty:{student_faculty}\n"
            
            file_object.write(content)
            print(f"Success: {student_name} was added to 'student_info.txt'")   
    
            more=input("Do you want to add more student(Yes/No)").lower()
            if more!="yes": # if more ="yes"  then false then dont go down to break or else go to while loop. Next case more =no then true go  to break
                break            
        
def get_all_students():
    try: 
        with open("file_handling\student_info.txt", "r") as file_object:
            student_info_list=file_object.readlines()  #returns list of line eg [line1, line2, ....]
            return student_info_list
                
    except FileNotFoundError:
        print("File not found!")
def update_student_by_id(search_roll):
    updated_lines = []  # only for search used here
    try:
        with open("file_handling\\student_info.txt", "r+") as file_object:
            lines = file_object.readlines()
            if lines:
                for line in lines:
                    if line.startswith(f"Roll:{search_roll}"):
                        updated_name = input("Enter updated Name:")
                        updated_faculty = input("Enter updated Faculty:")
                        updated_line = f"Roll:{search_roll}\tName:{updated_name}\tFaculty:{updated_faculty}\n"
                        updated_lines.append(updated_line)  # append() is the function of list, so appending
                    else:
                        updated_lines.append(line)
            else:
                print("File doesnot have student_info!")
            file_object.seek(0)    
            file_object.writelines(updated_lines)               
    except FileNotFoundError:
        print("File not found!")
    return updated_lines
    
    # with open("file_handling\student_info.txt","w") as file_object:
     
   
            
          
                   