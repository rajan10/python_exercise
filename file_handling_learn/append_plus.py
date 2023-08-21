# f=open('file_handling_learn\planet.txt', mode='a+')
# f.write('earth')
# print(f.tell())
# f.seek(0) # seek() will bring back the cursor to the position you specified
# print(f.read())

# append adds at last
f=open('file_handling_learn\planet.txt', mode='a+')
f.write('earth')
print(f.tell())
f.write()
f.seek(0) # seek() will bring back the cursor to the position you specified
print(f.read())
