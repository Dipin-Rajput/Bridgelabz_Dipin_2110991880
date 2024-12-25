# Map function

# The map () function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc.).

# Syntax: map(fun, iter)

# Parameters:

# fun: It is a function to which map passes each element of given iterable.
# iter:  iterable object to be mapped.

# Function to return double of n

def double(n):
    return n * 2

# Using map to double all numbers

numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))

# Same operation using lambda function

a = map(lambda x : x * 2, numbers)
print(a) # returns a map object, which can be converted into list or tuple.

# Using multiple iterables

def func(x, y):
    return x**y

b = map(func, [1, 2, 3], (2, 3, 2))
print(list(b))

# Built-in function with map

c = map(str.upper, ("a", "b"))
print(list(c))

d = map(round, [2.41, 3.22])
print(tuple(d))


# Filter function

# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

# Syntax: filter(function, sequence)

# Parameters:

# function: function that tests if each element of a sequence is true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.

# Define a function to check if a number is even

def is_even(n):
    return n % 2 == 0

# Define a list of numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to filter out even numbers

even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))

# Use filter to filter out numbers greater than 3

def fun(x):
    return x > 3

lst = filter(fun, numbers)
print("Greater than 3:", list(lst))

# Returning Upper case letter using filter

def f(x):
    return x.isupper()

str = ("a", "A", "b", "c", "d", "B", "X", "D","e")
upper = filter(f, str)
print("Upper-case letters:", list(upper))