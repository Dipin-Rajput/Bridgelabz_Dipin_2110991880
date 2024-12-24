# A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code.

# To create a Python module, write the desired code and save that in a file with .py extension.

def add(a, b):
    return a + b # Addition function

def sub(a, b):
    return a - b # Subtraction function

lst = [100, 20, 3, -40, 50]

# We can import the functions, and classes defined in a module to another module using the import statement in some other Python source file.
# When the interpreter encounters an import statement, it imports the module if the module is present in the search path.

# Search Path: Search path is a list of directories that the interpreter searches for importing a module.