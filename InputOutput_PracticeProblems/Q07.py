# 7) Accept any three strings from one input() call: Write a program to take three names as input from a user in a single input() function call.

# Input in 3 different variables

a, b, c = input("Enter names seperated by space: ").split()
print(f"First name: {a}, Second name: {b}, Third name: {c}")

# Input in list

lst = input("Enter names seperated by space: ").split()
print(lst)