# read sample.txt and print the number of lines
file = open("sample.txt", "r")
i = 0
for lines in file:
    i += 1

file.close()
print(i)