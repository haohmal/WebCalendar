# put your python code here
three_digit_integer = int(input())
digit_1 = three_digit_integer // 100
three_digit_integer = three_digit_integer % 100
digit_2 = three_digit_integer // 10
digit_3 = three_digit_integer % 10
print(digit_3 + digit_2 + digit_1)