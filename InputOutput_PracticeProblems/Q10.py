# 10) Read line number 4 from a file: Write a program to read the 4th line from a given file.

# readline()

# When there are no more lines to read, it returns an empty string ('').
# The line includes the newline character (\n) at the end unless it’s the last line.

with open("org.txt", "r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        if(line_number == 3): # It reads the next line in the file each time it's called.
            print(file.readline().strip()) # .strip() removes the newline character \n.
            break
