# 4) Remove first n characters from a string: Write a Python code to remove characters from a string from 0 to n and return a new string.

str = input("Enter your string: ")
n = int(input("Enter number of character you want to remove: "))

result = str[n:]
print("Your resulting string is:", result)