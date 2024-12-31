# 2) Print the Sum of a Current Number and a Previous number: Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

print("Sum of Current and Previous numbers:", end = " ")
for i in range(1, 11):
    print(i + i - 1, end = " ")