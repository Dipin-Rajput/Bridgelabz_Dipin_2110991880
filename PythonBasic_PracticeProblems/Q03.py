# 3) Print characters present at an even index number: Write a Python code to accept a string from the user and display characters present at an even index number.

str = input("Enter string: ")

print("String at even index: ", end = "")

for i in range(len(str)):
    if(i % 2 == 0):
        print(str[i], end = "")