file = open("test.txt", "w")
file.write("This line replaces everything in this file!")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()