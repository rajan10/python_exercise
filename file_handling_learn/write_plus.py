#writing and then reading from where it wrote

f=open('student_write.txt', mode='w+')
f.write('write')
f.write('write1')
f.write('write2')
print(f.tell()) # cursor position is 'after write2 and there is nothing after 'write2. so it will display nothing
f.write('helloworld')
f.seek(0)
print(f.read())


