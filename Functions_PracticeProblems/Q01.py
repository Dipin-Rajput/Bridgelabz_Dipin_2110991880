# 1) Create a function in Python: Write a program to create a function that takes two arguments, name and age, and print their value.

try:
    def data(a, b):
        print(f"Your name is: {a} and your age is {b}")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    data(name, age)
except:
    print("Unexpected Input")