# 1) Calculate the multiplication and sum of two numbers: Write a Python code to return the product of two numbers if the product is equal to or lower than 1000. Otherwise, return their sum.

first_number = int(input("Enter first number: "))
second_number = int(input("Enter Second number: "))

sum = first_number + second_number
product = first_number * second_number

if(product <= 1000):
    print("Product of two numbers is:", product)
else:
    print("Sum of two numbers is:", sum)
