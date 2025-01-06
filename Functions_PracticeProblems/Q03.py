# 3) Return multiple values from a function: Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def calc(x, y):
    return x + y, x - y

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

add, sub = calc(first, second)
print(f"Sum of two numbers is: {add}\nSubtraction of two numbers is: {sub}")