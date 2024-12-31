# 3) Calculate sum of all numbers from 1 to a given number.

num = int(input("Enter the number: "))
sum = 0

for i in range(1, num + 1):
    sum = sum + i
print("Sum of all numbers from 1 to given number is:", sum)