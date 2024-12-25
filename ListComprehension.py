# List Comprehension

# List comprehension is a way to create lists using a concise syntax. It allows us to generate a new list by applying an expression to each item in an existing iterable. This helps us to write cleaner, more readable code compared to traditional looping techniques.

# [expression for item in iterable if condition] # general syntax


numbers = [1, 2, 3, 4, 5, -6, -7, -8]

# Using list comprehension to create a new list using existing list number with different expression.

a = [x**2 for x in numbers]
print(a)

# It will create the list of boolean values.

b = [x % 2 == 0 for x in numbers]
print(b)

# This will enter the elements only divisible by 2.

c = [x for x in numbers if x % 2 == 0]
print(c)

# It will create the list of integers from 0 to 9

d = [i for i in range(10)]
print(d)

e = [[x, y] for x in range(3) for y in range(3)]
print(e)

# Flattening the list

f = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
g = [val for row in f for val in row]
print(g)