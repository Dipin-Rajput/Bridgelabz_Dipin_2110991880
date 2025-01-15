# 4) Reverse individual words

# Given string str, we need to print the reverse of individual words.

# Examples:

# Input : Hello World

# Output : olleH dlroW
# Find maximum difference between nearest left and right smaller elements

str = "Hello World"
lst = str.split(" ")

new_str = ""

stack = []

for i in lst:
    for j in i:
        stack.append(j)

    while(len(stack) > 0):
        new_str += stack.pop()

    new_str += " "

print("Reversed String:", new_str)