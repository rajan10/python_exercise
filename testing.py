my_dic_tuple_as_keys ={("Raj", 40):"Developer", ("Saj", 25):"IT support",("Sita", 35):"HouseWife"}
print(my_dic_tuple_as_keys)

my_set={"hello", "how", "are", "you"}
print(my_set)
print(id(my_set))

my_set.add("good")
print(my_set)
print(id(my_set))

my_frozen_set= frozenset(my_set)
print(my_frozen_set)
#my_frozen_set.add("Rajan")
#print(my_frozen_set)

print(dir(frozenset))