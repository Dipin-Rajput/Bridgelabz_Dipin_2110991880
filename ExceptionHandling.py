# Exception Handling

# Error: Error are problems in program due to which the program will stop the execution.
# Exception: Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.

# Some Built-in Python Exceptions

# 1. SyntaxError: It occurs when interpreter encounters a syntax error in the code, such as misspelled keyword, a missing colon, and unbalanced parenthesis.
# 2. TypeError: It occurs when an operation or function is applied to an object of the wrong type.
# 3. NameError: It occurs when a variable or function name is not found in the current scope.
# 4. IndexError: It occurs when an index is out of range.
# 5. KeyError: It occurs when key is not found in a dictionary.

# a = 45
# if(a > 50)
# print("a is greater.") # This will cause a syntax error.

# marks = 100
# print(marks/0) # This will raise ZeroDivisionError exception.

# Handling ZeroDivisionError exception using try-except block.

try:

    marks = 97
    if(marks < 100):
        marks = marks / 0

except:
    print("Error Occured: You are trying to divide by 0")

print("Program Running after exception caught in try and except block")
print()

# Handling Index out of range with try and except.
a = [1, 2, 3]

try:
    for i in range(4):
        print("Element:", a[i])
except:
    print("Error: Index out of range.")
print()

# Multiple except statement: A try statement can have more than one except clause, to specify handlers for different exceptions. But at most one handler will be executed.

def fun(a):

    if(a > 50):
        print(b) 
        b = a/(a - a)
    print("Value of b is:", b)

# We added two exception below but as soon as try block identified the first one, it skips all the statement and passed it to except statement.

try:
    fun(89)
    fun(37)
except ZeroDivisionError:
    print("You are trying to divide by 0.")
except NameError:
    print("Variable not defined.")
