my_list=[]
attributes_and_funct= dir(my_list)
attributes_and_funct1=str(attributes_and_funct)
my_function=[x for x in attributes_and_funct1 if x is not callable(getattr(my_list,attributes_and_funct1))]
print(my_function)