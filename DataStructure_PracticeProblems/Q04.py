# 4) Count the occurrence of each element from a list.

# Given:
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Expected Output:
# Printing count of each item {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count = {}

for i in sample_list:
    x = sample_list.count(i)
    count[i] = x

print("Count of each element is:", count)
