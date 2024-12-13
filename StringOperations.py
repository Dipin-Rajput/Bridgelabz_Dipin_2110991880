# String is a datatype that stores the sequence of characters.
# String in Python can be defined using single quotes, double quotes and triple quotes.

a = 'Python'
b = "is a"
c = """Programming languange"""

print(a, b, c)
print()

# String Concatination

print(a + b + c)
print()

print(a + " " + b + " " + c) # Providing sapcing between the string.
print()

# Escape sequence

print("Python is high level programming language.\nThis is the new line.") # \n for the new line.
print()

print("Python is high level programming language.\tThis is the new line.") # \t for the tab space.
print()

# length function

print("The length of string:", c, "is", len(c))
print()

# Indexing: It always starts from 0 in python, each and every character has a index assigned to it.
# Python also supports negative indexing, which starts from end, with -1, -2, ... and so on

str = "chitkara university"

print(str[0])
print(str[-1])
print()

# str[3] = "a" (It is not possible because String does not support item assignment)

# Slicing: Dividing string into substring with help of indexes.
# eg: str[start_index : end_index], end index is not included

print(str[1 : 5])

# It can be used in many ways, such as only with start index, only with end index, also with negative indexes.

print(str[6 : ]) # If end index is not provided python will automatically take the length of the string in this case it is 19.
print(str[ : 7]) # If start index is not provided it will start from 0.

print(str[-8 : -5]) # but print(-5 : -8) it will not work it will not print the character in reverse order.
print()

# String Functions

# 1. str.endswith(): return true if string ends with substr
# 2. str.capitalize(): it capitalizes 1st character of string
# 3. str.replace(old, new): replaces all occurrences of old string with the new
# 4. str.find(): returns the 1st index of 1st occurrence
# 5. str.count(): counts the occurrence of substr

print(str.endswith("sity"))
print(str.capitalize()) # It doesn't do the changes in the same string, it creates a new string.
print(str)

print(str.replace("i", "x"))
print(str)

print(str.find("a"))
print(str.count("s"))







