def find_maximum_of_3(x,y,z):
    if x>y and x>z:
        print(f"{x} is the highest of all 3 nos")
    elif y>x and y>z:
        print(f"{y} is the highest number")
    else:
        print(f"{z} is the highest number")
        
print(find_maximum_of_3(10,-2,3))