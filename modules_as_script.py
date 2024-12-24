# Modules can act as standalone scripts or be imported by other scripts.

# if __name__ == "__main__":
#     # Code here runs only if this file is executed directly.

# modules_as_script.py

def hello():
    print("Hello from the script!")

if __name__ == "__main__":
    print("This script is being executed directly!") # This will be printed and function call will take place, if run this file as script.
    hello()

# import modules_as_script

# modules_as_script.hello()
 
# If we import this module into another file only hello function will work.
# Outputs: Hello from the script! because the main() function is only executed when my_module.py is run as a script.

