# file_obj=open("example.txt", "w")
# file_obj.write("Hellow world")
# file_obj.close()


def read_file():
    try:
        file_obj=open("example.txt", "r")
        read_content= file_obj.read()
        print(read_content)
    except FileNotFoundError:
        print("File not found")
        
def write_file():
    file_obj = open("example.txt","w")
    file_obj.write("Nepal is beautiful")
    
    
    
    
    ""Desigin class Student_file_handler with expected methods in it
    wrtie as many function as you want with different 
    
    
    
    
    # 
    
    print("""1. Read student?  if no student there are no student
             2. Add student  input from terminal : Name, roll, faculty
             3. Show all Students
             4. Quit
             Type number(1,2,3) to  select options"""
           )
    take studnet info from terminal.
    
    write_file()
    
    program : main.py
   