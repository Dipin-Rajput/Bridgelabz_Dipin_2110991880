# 4) Print multiplication table of a given number.

num = int(input("Enter the number you want multiplication table of: "))

for i in range(1, 11):
    print(num, "X", i, "=", num * i)