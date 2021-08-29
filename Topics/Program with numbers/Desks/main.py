class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

desks = class_1 // 2 + class_1 % 2
desks += class_2 // 2 + class_2 % 2
desks += class_3 // 2 + class_3 % 2

print(desks)