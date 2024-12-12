# Print Statement

print("Hello World")
print(45 + 39)
print()

# Variables

Name = "Dipin"
Age = 26
Price = 52.35
bool = True
a = None

print("My Name is:", Name)
print("My Age is:", Age)
print("Price given is:", Price)
print()

# Datatypes

print(type(Name))
print(type(Age))
print((type(Price)))
print(type(bool))
print(type(a))
print()

# Operators

# Arithmetic Operators: +, -, *, /, %, **

x = 5
y = 2

print("Sum of x and y is", x + y)
print("Diff of x and y is:", x - y)
print("Mul of x and y is:", x * y)
print("Div of x and y is:", x / y)
print("Modulo of x and y is:", x % y)
print("x raise to power y is:", x ** y)
print()

# Relational Operators: ==, !=, >=, <=, >, <

print(x == y)
print(x > y)
print(x < y)
print(x != y)
print(x >= y)
print(x <= y)
print()

# Assignment Operators: +=, -=, *=, /=, %=, **=

# x = x + 5

x += x
print("x is: ", x)

x -= x
print("x is: ", x)

y *= y
print("y is: ", y)

y /= y
print("y is: ", y)

y **= y
print("y is: ", y)

y %= y
print("y is: ", y)
print()

# Logical Operators: not, and, or

a = 47
b = 59

print(not a != b)
print(a < b and a != b) #True
print(a > b and a != b) #False
print(a > b or a != b) #True
print()

# Type Conversion

# Implicit type conversion

m = 10
n = 14.32

sum = m + n
print(sum) # 24.32
print()

# Type Casting

l = 6.4
l = int(l)
print(l)

k = 100
k = float(k)
print(k)

q = 147
q = str(q)
print(type(q), q)
print()

# User Input

c = input("Enter your Name: ")
print("Welcome", c)
print()

c = input("Enter any Number: ") # input always return output of string datatype.
print(type(c), c)
print()

c = int(input("Enter any Number: ")) # Similarly float can be used in the place of int for floating value input.
print(type(c), c)
print()








