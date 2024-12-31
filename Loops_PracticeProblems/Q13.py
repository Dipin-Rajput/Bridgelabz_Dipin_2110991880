# 13) Find the factorial of a given number.

num = int(input("Enter the number you want factorial of: "))
fact = 1

for i in range(num, 0, -1):
    fact = fact * i

print("Factorial of given number is:", fact)