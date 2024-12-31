# 6) Display numbers divisible by 5: Write a Python code to display numbers from a list divisible by 5.

lst = [55, 46, 78 ,95, 53, 42, 39, 80, 70, 35]

print("Elements divisible by 5 are:")
for i in lst:
    if(i % 5 == 0):
        print(i)