# 8) Format variables using a string.format() method: Write a program to use string.format() method to format three variables.

# Name indexes

print("My name is {name}, I am {age} year's old, I live in {country}".format(name = "John", age = 21, country = "Amercia"))

# Index number

print("My name is {2}, I am {0} year's old, I live in {1}".format("John",21, "Amercia"))

# Empty placeholder and colon

print("My name is {}, I am {:} year's old, I live in {}".format("John",21, "Amercia"))

# Alternate

my_string = "My name is {0}, I am {1} year's old, I live in {2}"
print(my_string.format("John", 21, "Amercia"))
