# write the code here
input_string = input()
file = open("input.txt", "w", encoding="utf-8")
file.write(input_string)
file.close()