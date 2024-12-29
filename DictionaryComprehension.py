# Dictionary Comprehension

# Dictionary comprehension allows you to create a dictionary in a similar concise manner, where you specify both the keys and the values in one line.

# Syntax: {key_expression: value_expression for item in iterable if condition}s

myDict = {x: x**2 for x in [1,2,3,4,5]} # similarly we can use range function instead of list.
print (myDict)

sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)

# Conditionla statements in dictionary comprehension

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

# Swapping keys and values.

dict = {1 : "name", 2 : "age", 3 : "city"}

swap = {v : k for k, v in dict.items()}
print(swap)

# Nested Dictionary

nested_dict = {x: {x: x**2} for x in range(5)}
print(nested_dict)