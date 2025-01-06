# 5) Accept a list of 5 float numbers as an input from the user: Write a program to accept a list of 5 float numbers from the user.

lst = list(map(float, input("Enter 5 float numbers: ").split()))
print(lst)