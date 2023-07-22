def reverse_string(input_string):
  reveresed_string=""
  for char in input_string:
    reveresed_string=char+reveresed_string
  return reveresed_string

print(reverse_string("hello"))

