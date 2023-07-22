def string_to_dict(string):
    char_dict={}
    for char in string:
        if char not in char_dict.keys():
            char_dict[char]=1
        else:
            char_dict[char]=char_dict[char]+1
    return char_dict

print( string_to_dict("elephant"))