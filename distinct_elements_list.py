def distinct_elements_list(my_list):
    unique_elements=[]
    for i in my_list:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements


my_list=[1,2,3,3,3,3,4,4,5]
print(distinct_elements_list(my_list))