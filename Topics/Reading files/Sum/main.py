# read sums.txt
file = open("sums.txt", "r")
for line in file:
    numbers = line.split(" ")
    if len(numbers) >= 2:
        print(int(numbers[0]) + int(numbers[1]))

file.close()