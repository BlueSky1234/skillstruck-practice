file = open('test.txt', 'a')
file.write("This is the new line we added!")
file.close()

file = open('test.txt', 'r')
print(file.read())
file.close()