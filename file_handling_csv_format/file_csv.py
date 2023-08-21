import csv
with open("file_handling_csv_format\employees.csv","r") as  csv_file_object:
    #delimiter is a seperator used to distinguish one field or value from another in csv comma is a seperator, in TSV tab is the delimiter
    # employee_reader = csv.reader(csv_file_object, delimiter=' ', quotechar='|')
    employee_reader = csv.reader(csv_file_object)
    for row in employee_reader:
        # print(', '.join(row))
        print(row)


with open("file_handling_csv_format\employees.csv","a") as  csv_file_object:
    employee_writer=csv.DictWriter(csv_file_object, fieldnames=['First Name','Last Name','Email','Phone','Gender','Age','Job Title','Years Of Experience','Salary','Department'])
    employee_writer.writerow({'First Name':'Ram1', 'Last Name':'Nepali','Email':'ram_nepali@slingacademy.com','Phone':'(871)098-2647x80448','Phone':'male','Age':'28','Job Title':'Python Developer','Years Of Experience':'3','Salary':'8500','Department':'Product'})
    
with open("file_handling_csv_format\employees.csv","r") as  csv_file_object:
    reader = csv.DictReader(csv_file_object) 
    for row in reader:
        print(row)
        
       
  
    
    