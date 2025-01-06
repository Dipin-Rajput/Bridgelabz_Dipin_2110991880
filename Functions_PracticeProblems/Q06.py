# 6) Create a recursive function: Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def recursive_func(i):
    if(i >= 0):
        res = i + recursive_func(i - 1)
    else:
        res = 0
    return res

sum = recursive_func(10)
print(f"Recursive Sum of numbers from 0 to 10 is: {sum}")