# 5) Create a Python set such that it shows the element from both lists in a pair.

# Given:

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# Expected Output:
# Result is {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

res = set()

for i in range(len(first_list)):
    res.add((first_list[i], second_list[i]))

print("Result is:", res)

