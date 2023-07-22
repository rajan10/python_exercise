def print_even_number_from_list(my_list):
    even_list=[]
    for i in my_list:
        if (i%2==0):
            even_list.append(i)
    return even_list

my_list=[1,2,3,4,5,6,7,8]
print(print_even_number_from_list(my_list))