# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
num_groups = int(input())
i = 0
kindergarten = {}
for i in range(9):
    if i < num_groups:
        size = int(input())
    else:
        size = None
    kindergarten[groups[i]] = size

print(kindergarten)
