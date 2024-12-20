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
print()

# Try with else clause

# In Python, we can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

def check(a, b):

    try:
        print((a+b)/(a-b))
    except:
        print("Error found.")
    else:
        print("No error found.")

check(2, 3) # Else statement will run, since no exception found.
check(3, 3) # except statement will run, since exception found.
print()

# Finally Keyword in Python

# Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after the normal termination of the try block or after the try block terminates due to some exception. The code within the finally block is always executed.

def opr(a, c):
    
    try:
        b = a/(a-c)
        print(b)
    except ZeroDivisionError:
        print("You are dividing by 0.")
    else:
        print("No error found.")
    finally:
        print("This statement will always print.")

opr(4, 4)
opr(5, 4)
print()

# Raise Exception

# The raise statement allows the programmer to force a specific exception to occur.

try:
    age = int(input("Enter your age: "))
    if(age >= 18 and age <= 24):
        print("You are eligible.")
    else:
        raise Exception("Over age.") # This will raise the exception in case age is out of limit.
        
except:
    print("You are not eligible")
print()

# Now to print exception we get.

try:
    age = int(input("Enter your age: "))
    if(age >= 18 and age <= 24):
        print("You are eligible.")
    else:
        raise Exception("Over age.") # This will raise the exception in case age is out of limit.
        
except Exception as e: # This will print the exception.
    print("You are not eligible:", e)


