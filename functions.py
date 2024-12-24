# Functions

def print_name(n):
    print(n*2)

print_name("Hello")

# Function in python defined using def keyword, then function name alogside with arguments.

# def f_name(a, b, c): # (Positional Arguments)
    # return a + b + c
# a = f_name(5, 6, 8) # (function calling)
# print(a)

# We need to store the output in variable if we are using return statement inside the function.

# Default Arguments

# when we directly assign the values to the arguments using '=' to operator, then it is known as default arguments.

def f_name(a, b = 55, c = 33):
    return a + b + c
a = f_name(22, 1, 2)
print(a)

# Whether we pass any value in defualt arguments, but if their is values in keyword arguments it consider that only, if we not provide value in keyword arguments, then it consider the values of default arguments.

def f(a = 11, b = 55, c = 33):
    return a + b + c
a = f()
print(a)

# Scope in python

# Global Scope: It is defined as the scope which is available through out the program.
# Local Scope: It is defined as the scope which is available inside the particular block for eg: functions, loops, if-elif-else statements.

# Example: 1

x = 0 # Global scope
def f1():
    x = 10 # Local scope
    print(x)

print("Value of x is:", x)
f1()

# Example: 2

x = 10
def f1(x):
    print("x is:", x)
    x += 10
    print("x is:", x)
    x *= 20
    print("x is:", x)

f1(x)
print("x final value is:", x)

# Example: 3

# Global Keyword

x = 10
def f1():
    global x # To access the global variable inside the function to access or modifies its values.
    print("x is:", x)
    x += 10
    print("x is:", x)
    x *= 2
    print("x is:", x)
f1()
print("final value of x is:", x)





