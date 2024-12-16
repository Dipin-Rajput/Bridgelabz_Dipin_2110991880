Date - 13-12-2024

Topics Covered:

# String

# Datatype

String is a datatype that stores the sequence of characters.
String in Python can be defined using single quotes, double quotes and triple quotes.

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

# Indexing

It always starts from 0 in python, each and every character has a index assigned to it.
Python also supports negative indexing, which starts from end, with -1, -2, ... and so on

str = "chitkara university"

print(str[0])
print(str[-1])
print()

str[3] = "a" (It is not possible because String does not support item assignment)

# Slicing
 
Dividing string into substring with help of indexes.
eg: str[start_index : end_index], end index is not included.

print(str[1 : 5])

It can be used in many ways, such as only with start index, only with end index, also with negative indexes.

print(str[6 : ]) (If end index is not provided python will automatically take the length of the string in this case it is 19.)
print(str[ : 7]) (If start index is not provided it will start from 0.)

print(str[-8 : -5]) (but print(-5 : -8) it will not work it will not print the character in reverse order.)
print()

# String Functions

1. str.endswith(): return true if string ends with substr
2. str.capitalize(): it capitalizes 1st character of string
3. str.replace(old, new): replaces all occurrences of old string with the new
4. str.find(): returns the 1st index of 1st occurrence
5. str.count(): counts the occurrence of substr

print(str.endswith("sity"))
print(str.capitalize()) (It doesn't do the changes in the same string, it creates a new string.)
print(str)

print(str.replace("i", "x"))
print(str)

print(str.find("a"))
print(str.count("s"))



# Conditional Statements

# Conditional Statements: if - elif - else

1. WAP to check if a number entered by the user is odd or even.

a = int(input("Enter any number: "))

if(a % 2 == 0):
    print("It is an even number.")
else:
    print("It is an odd number.")
print()


2. WAP to find the greatest of 3 numbers entered by the user.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if(x >= y and x >= z):
    print("Greatest number is:", x)
elif(y >= x and y >= z):
    print("Greatest number is: ", y)
else:
    print("Greatest number is:", z)
print()


3. WAP to check if a number is a multiple of 7 or not

b = int(input("Enter any number: "))

if(b % 7 == 0): 
    print("It is the multiple of 7.")
else:
    print("It is not the multiple of 7.")
print()


# Nested if

age = 28

if(age >= 18):
    if(age <= 24):
        print("Eligible for Job.")
    else:
        print("Not eligible for Job")
else:
    print("Under age")


# Loops

1. WAP to print the square of first 10 numbers.

i = 1

while(i <= 10):
    print(i * i)
    i+=1

# for loop with break and continue

# break statement breaks the loop when the condition is met.
# continue statement skip the iteration when the condition is met.

str = "DipinRajput"

for i in str:
    if(i == "a"):
        break
    else:
        print(i)
print()

for i in str:
    if(i == "i"):
        continue
    else:
        print(i)
print()
