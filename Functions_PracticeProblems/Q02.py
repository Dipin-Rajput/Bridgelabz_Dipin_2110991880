# 2) Create a function with variable length of arguments: Write a program to create function func1() to accept a variable length of arguments and print their value.

def func(*args):
    print("Function with variable length of arguments and its values:", args)

func(1, 2, 3, "Dipin", "Chitkara", 4, 5)