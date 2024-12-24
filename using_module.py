# To import the module modules.py, we need to put the following command at the top of the script.

import modules

# (import) does not import the functions or classes directly instead imports the module only. To access the functions inside the module the dot(.) operator is used

print(modules.add(5, 2)) # Importing add function from modules.py
print(modules.sub(5, 2)) # Importing sub function from modules.py
print(modules.lst[3]) # Printing list element from modules.py

# Using from statement with import

# Python’s from statement lets you import specific attributes from a module without importing the module as a whole.

from modules import add

print(add(7, 8)) # Using from statement allow us to directly use attribute instead of dot(.) operator

from modules import * # The * symbol used with the import statement is used to import all the names from a module to a current namespace.

# Python interpreter searches for the module in the following manner:

# 1. First, it searches for the module in the current directory.
# 2. If the module isn’t found in the current directory, Python then searches each directory in the shell variable PYTHONPATH. The PYTHONPATH is an environment variable, consisting of a list of directories.
# 3. If that also fails python checks the installation-dependent list of directories configured at the time Python is installed.

# importing sys module

import sys

# importing sys.path

print(sys.path) # sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search for the required module.

# Renaming the python module

# We can rename the module while importing it using the keyword.

import modules as m

print(m.add(4, 8))
print(m.sub(78, 91))

# Built-in modules

import math

print(math.sqrt(25)) # using square root(sqrt) function contained in math module

print(math.pi) # using pi function contained in math module
 
print(math.factorial(4))  

# importing built in module random

import random

# printing random integer between 0 and 5

print(random.randint(0, 5))  

# print random floating point number between 0 and 1

print(random.random())  

# random number between 0 and 100

print(random.choice(["True", "False"]))

# dir() function

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

import modules

x = dir(modules)
print(x)

# Package:

# A package is a collection of Python modules under a common namespace. In practice, it is a directory that contains a special file __init__.py (which may be empty) and one or more module files and sub-packages. Packages allow for a hierarchical structuring of the module namespace using dot notation (e.g., package.module).

# Dunder/Magic Methods

# Special methods with double underscores (e.g., __init__, __str__).

# Used to define custom behavior for built-in operations.

# Common examples:

# __init__: Called when creating an instance of a class.
# __str__: Returns a string representation of an object.

#  Compiled Python Files

# When you import a module, Python compiles it into bytecode (optimized format).
# Compiled files are stored in the __pycache__ directory with a .pyc extension.
# Faster subsequent execution.
# Automatically updated when the source code changes.

# venv

# A virtual environment is an isolated Python environment that allows you to:

# Install and manage project-specific dependencies without affecting the global Python installation.
# Avoid conflicts between dependencies of different projects.
# Use different versions of the same library in different projects.

# requirement.txt

# A requirements.txt file is a text file that lists all the Python packages (and their versions) that your project needs. It allows others (or future you) to recreate the exact environment needed to run your project.
