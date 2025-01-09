# Inheritance

class Person: # Parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname, end = " ")

# class Student(Person):
#     pass

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function: either using parents name or using super()

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        # super().__init__(fname, lname)
        self.year = year # adding properties
    
    def welcome(self):
        print("Welcome to the class of:", self.year) # method in child class

x = Student("John", "Doe", 2020)
x.printname()
x.welcome()

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.


# Private Variables

# In Python, private variables are not strictly enforced, but you can use naming conventions to indicate that a variable is intended to be private and should not be accessed directly outside the class. Python relies on name mangling to make variables somewhat "private" by altering their names when they are declared with a double underscore prefix (__).

# 1. Private Variables (Name Mangling)

# Variables with a double underscore (__) prefix are mangled by Python to make them harder to access from outside the class.
# This doesn't prevent access but makes the variable name less predictable and harder to accidentally access.

class MyClass:
    def __init__(self):
        self.__private_variable = 42  # Private variable

    def public_method(self):
        print(f"Accessing private variable inside method: {self.__private_variable}")
        

obj = MyClass()

# Accessing from inside the class method
obj.public_method()  # Output: Accessing private variable inside method: 42

# Trying to access directly outside the class (not recommended)
# print(obj.__private_variable)  # AttributeError: 'MyClass' object has no attribute '__private_variable'

# Name Mangling:

# Python internally changes the name of private variables by adding _ClassName before the variable name.
# For example, self.__private_variable becomes self._MyClass__private_variable.

print("Accessing private variable using mangled name:", obj._MyClass__private_variable)

# 2. Single Underscore (_) Convention

# Variables with a single underscore (_) prefix are not private but indicate that the variable is protected and should be treated as internal to the class or module.
# This is more of a convention than a strict rule and doesn't prevent access.

class MyClass:
    def __init__(self):
        self._protected_variable = 99  # Protected variable

obj = MyClass()
print(obj._protected_variable)  # Output: 99


# Iterators

class MyNumbers:
    def __iter__(self):
      self.a = 1
      return self

    def __next__(self):
      x = self.a
      self.a += 1
      return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Iterators with StopIteration

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# Generator

def generator():
   yield 1
   yield 2
   yield 3

for i in generator():
   print(i)

# x = generator()

# print(next(x))
# print(next(x))

# Example

def f(max):
    cnt = 1
    while(cnt <= max):
       yield cnt
       cnt += 1

ctr = f(5)
for n in ctr:
   print(n)

# Decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()