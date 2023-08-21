
#reads and the cursor is at the place where read is
f= open('file_handling_learn\planet.txt', mode='r+')
print(f.tell())
data =f.read() 
print(data)
print(f.tell())
new_data=f.write('Pluto')
print(f.tell())
print(f.read())

# print(data)
# print(f.tell())