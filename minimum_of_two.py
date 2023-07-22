def minimum_of_two(x,y):
    if x<y:
        return x
    return y

def minimum_of_three(x,y,z):
    return minimum_of_two(x, minimum_of_two(y,z))


print(minimum_of_three(50, 10, 90))