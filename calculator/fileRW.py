file = open("output.txt", "w")
file.write("This line was written to the file.")
file.close()

file = open("output.txt", "r")
print(file.read())
file.close()

file = open("output.txt", "a")
file.write("\nSecond line written to the file.")
file.close()

file = open("output.txt", "r")
print(file.read())
file.close()
