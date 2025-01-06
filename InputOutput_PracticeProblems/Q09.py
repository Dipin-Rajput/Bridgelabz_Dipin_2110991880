# 9) Check if a file is empty or not: Write a program to check if the given file is empty.

file = open("empty.txt", "x")

with open("empty.txt", "r") as f:
    f.read()
    if(f.tell() == 0):
        print("File is Empty")
    else:
        print("File is not Empty")