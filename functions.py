# Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def print_name(n):
    print(n*2)

print_name("Hello")


# Arguments

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.


# Function in python defined using def keyword, then function name alongside with arguments.

# --------------------------------------------------------------------------------------------------------------------------------

# def f_name(a, b, c): # (function definition)
    # return a + b + c
# a = f_name(5, 6, 8) # (function calling)
# print(a)

# (a, b, c) are the arguments in function definition
# We need to store the output in variable if we are using return statement inside the function.

# --------------------------------------------------------------------------------------------------------------------------------


# Parameters or Arguments?

# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def function_name(x, y): # Parameters
    print(f"X is {x} and Y is {y}")

function_name(57, 49) # Arguments


# Four types of Arguments in Python


# 1. Positional Arguments:

# Arguments are passed to the function in the order they are defined in the function signature.
# The function assigns values to parameters based on their position.
# These are the most common and straightforward way to pass arguments.

def sum(a, b, c):
    print(f"Sum is: {a + b + c}")

sum(5, 7, 9) # Positional Arguments

# ----- Positional Only Arguments -----

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
 
def my_function(x, /):
    print(x)

my_function(3)
# my_function(x = 3) # This will give syntax error


# 2. Keyword Arguments:

# Arguments are passed using parameter names explicitly.
# The order of the arguments does not matter because the function matches them by their names.

def sub(a, b):
    print(f"Subtraction is: {a - b}")

sub(b = 97, a = 45) # Keyword Arguments

# ----- Keyword-Only Arguments -----

# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
    print(x)

my_function(x = 3)
# my_function(3) # This will give error

# Combining Positional and Keyword Arguments:

# You can use both types in the same function call, but positional arguments must come before keyword arguments.

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("Alice", last_name="Smith")  # Mixing positional and keyword arguments
# greet(first_name="Alice", "Smith")  # This will raise a SyntaxError


# 3. Default Arguments:

# Programmer set the default value for a parameter in the function definition, using '=' to operator.
# If the caller omits the argument, the default value is used.

def f_name(a, b = 55, c = 33):
    return a + b + c
a = f_name(22, 1, 2)
print(a)

# Whether we pass any value in defualt arguments, but if their is values in keyword arguments it consider that only, if we not provide value in keyword arguments, then it consider the values of default arguments.

def f(a = 11, b = 55, c = 33):
    return a + b + c
a = f()
print(a)


#  4. Variable Length Arguments:

# In Python, variable-length arguments allow a function to accept an arbitrary number of arguments. This is useful when you don't know in advance how many arguments will be passed to the function.

# i) *args for Non-Keyword Arguments:

# Used to accept a variable number of positional arguments.
# Captures all extra positional arguments passed to the function as a tuple.

def brand(*args):
    print(f"Cars of Different brands: {args}")

brand("Audi", "Mahindra", "Maruti") # Positional Arguments

# ii) **kwargs for Keyword Arguments:

# Used to accept a variable number of keyword arguments.
# Captures all extra keyword arguments passed to the function as a dictionary.

def func2(**kwargs):
    print("Keyword arguments:", kwargs)

func2(a=1, b=2, c=3)       # Keyword arguments: {'a': 1, 'b': 2, 'c': 3}


# Combining *args and **kwargs

# You can use both *args and **kwargs in the same function to handle a mix of positional and keyword arguments.

def func3(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

func3(1, 2, 3, a="x", b="y", c="z")


# Passing a List as an Argument

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_func(food):
    for x in food:
        print(x, end = " ")
    print()

fruits = ["apple", "banana", "cherry"]

my_func(fruits)


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