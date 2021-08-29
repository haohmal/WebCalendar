# the list "walks" is already defined
# your code here
walking_sum = 0
for day in walks:
    walking_sum += day['distance']

print(walking_sum // len(walks))