def palindrome_check(input_string):
    reverse_string=""
    for char in input_string:
        reverse_string+= char
    if input_string==reverse_string:
        print(f"{input_string} is palindrome")
    else:
        print(f" {input_string} is not a palindrome")

print(palindrome_check("madams how are you"))