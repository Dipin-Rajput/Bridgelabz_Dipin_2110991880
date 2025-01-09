# Classes and Objects


# Classes:

# A class in Python is a user-defined template for creating objects. It bundles data and functions together, making it easier to manage and use them
# Classes are blueprint for creating objects, they encapsulates data (attributes) and behaviours (method).


# Objects: An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

class Dog:
    sound = "bark" # class attribute: It is shared across all instances of Dog class

x = Dog() # Creating object

# print(x.sound) # Accessing sound using object
# print(Dog.sound) # Accessing sound using class name because it is a class attribute

# Using __init__() Function

# In Python, class has __init__() function. It automatically initializes object attributes when an object is created.


# Self Parameter

# self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.

class Dog:
    species = "canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "bark"

    def noise(self):
        print("Dog's sound:", self.sound)
        

dog1 = Dog("ruff", "5")

print(f"Name is: {dog1.name} and Age is: {dog1.age}")
print("Dog species:", dog1.species)
dog1.noise()


# __str__ Method

# __str__ method in Python allows us to define a custom string representation of an object. By default, when we print an object or convert it to a string using str(), Python uses the default implementation, which returns a string like <__main__.ClassName object at 0x00000123>.

class Cat:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __str__(self):
        return f"Cat name is: {self.name} and Cat sound is: {self.sound}" # Returning a string

cat1 = Cat("Fluf", "mew")
cat2 = Cat("Rose", "mew")

print(cat1)


# Namespace

# Simply it is the collection of names.
# A namespace is a system that has a unique name for each and every object in Python.

# Types of namespace:

# 1. Built-in: Always available any part of program.
# 2. Global namespace: Creation of each module create global namespace.
# 3. local namespace: Modules have various functions and classes, it is created when fuction is called.


# Scope

# 1. built-in

# The built-in scope contains Python's built-in functions and objects like len, print, str, etc.
# These are available everywhere in your code unless explicitly overridden.

# 2. local

# Variables defined inside a function are in the local scope.
# They can only be accessed within that function.
# These variables are created when the function is called and destroyed when the function ends.

def fun():
    x = 10 # local scope
    print(x)

fun()

# 3. enclosing

# Variables defined in an enclosing function (a function that contains another function) are in the enclosing scope.
# These variables are accessible to inner (nested) functions.
# Use the nonlocal keyword to modify enclosing variables inside a nested function.

def outer():
    x = 10 # enclosing scope
    def inner():
        nonlocal x
        x += 10

        print("Inner:", x)
    
    inner()
    print("Outer:", x)

outer()

# 4. global

# Variables defined at the top level of a module (outside any function or class) are in the global scope.
# They are accessible throughout the module, including inside functions and classes (unless shadowed by local variables).
# Use the global keyword to modify global variables inside a function.

x = 10 # global scope

def func():
    global x # global keyword to modify the value of global variable

    x += 10
    print(x)

func()
print(x)


# Class Objects

# Defined using the class keyword.
# Can include methods, class attributes, and properties.

class Example:

    counter = 0

    def __init__(self):
        Example.counter += 1

# Instance Objects

o1 = Example() # Created by calling a class like a function.
o2 = Example() # Hold unique data per instance.

print(o1.counter)


# Class Variables

# These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.

class Temp1:
    class_variable = 45
    pass

# Instance Variables

# Variables that are unique to each instance (object) of a class. These are defined within __init__ method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.

class Temp2:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"Your full name is: {self.fname} {self.lname}"
    
name1 = Temp2("Dipin", "Rajput")
name2 = Temp2("Rohan", "Sharma")

print(name1)
print(name2)