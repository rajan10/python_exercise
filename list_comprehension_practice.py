"""Original List: [2, 5, 8, 3, 10]
Modified List: [1.4142135623730951, 125, 2.8284271247461903, 27, 3.1622776601683795]
    """
import math

def sqrt_even_cube_odd(my_num_list):
    modified_list=[math.sqrt(x) if x%2==0 else x**3 for x in my_num_list ]
    return modified_list

new_list=sqrt_even_cube_odd([2, 5, 8, 3, 10])
print(new_list)