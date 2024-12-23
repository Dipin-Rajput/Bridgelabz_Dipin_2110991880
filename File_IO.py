# File Handling Operations in Python

# 1. Opening Files

file = open('example.txt', 'r')  # Open for reading
file = open('example.txt', 'w')  # Open for writing
file = open('example.txt', 'a')  # Open for appending
file = open('example.txt', 'rb')  # Open in binary read mode
file = open('example.txt', 'wb')  # Open in binary write mode

# 2. Closing Files

file = open('example.txt', 'r')
file.close()  # Always close files after use to free resources

# 3. Reading Files

# 3.1 Reading the entire file

with open('example.txt', 'r') as file:
    content = file.read()
    print("Reading the entire file:")
    print(content)

# 3.2 Reading line by line

with open('example.txt', 'r') as file:
    print("\nReading file line by line:")
    for line in file:
        print(line.strip())

# 3.3 Reading a specific number of characters

with open('example.txt', 'r') as file:
    print("\nReading the first 10 characters:")
    content = file.read(10)
    print(content)

# 3.4 Using readlines()

with open('example.txt', 'r') as file:
    print("\nReading all lines using readlines():")
    lines = file.readlines()
    print(lines)

# 4. Writing to Files

# 4.1 Overwriting the entire file

with open('example.txt', 'w') as file:
    file.write("This is a new line.\n")
    file.write("Writing another line.")

# 4.2 Writing binary data

with open('example.bin', 'wb') as file:
    file.write(b"This is binary data.")

# 5. Appending to Files

# 5.1 Adding content without overwriting

with open('example.txt', 'a') as file:
    file.write("\nAdding a new line at the end.")

# 6. File Positioning

with open('example.txt', 'r') as file:
    print("\nChecking and changing file position:")
    print(f"Current position: {file.tell()}")  # Get the current position
    file.seek(5)  # Move to the 5th byte in the file
    print(f"Content from new position: {file.read()}")  # Read from the new position

# 7. Working with Binary Files

# 7.1 Reading binary files

with open('example.bin', 'rb') as file:
    print("\nReading binary file:")
    data = file.read()
    print(data)

# 7.2 Writing binary files

with open('example.bin', 'wb') as file:
    file.write(b"Binary data")

# 8. Checking File Existence

import os

if os.path.exists('example.txt'):
    print("\nFile exists.")
else:
    print("\nFile does not exist.")

# 9. Deleting Files

if os.path.exists('example.txt'):
    os.remove('example.txt')  # Delete the file
    print("\nFile deleted.")
else:
    print("\nFile does not exist.")

# 10. Other File Operations

# 10.1 Renaming a file

if os.path.exists('old_name.txt'):
    os.rename('old_name.txt', 'new_name.txt')
    print("\nFile renamed.")
else:
    print("\nFile to rename does not exist.")

# 10.2 Creating an empty file

with open('empty_file.txt', 'w') as file:
    pass  # Creates an empty file
    print("\nEmpty file created.")
