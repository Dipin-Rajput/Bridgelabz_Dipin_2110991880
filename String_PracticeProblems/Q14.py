# 14) Split a string on hyphens.

# Given: str1 = "Emma-is-a-data-scientist"

# Expected Output: Displaying each substring:

# Emma
# is
# a
# data
# scientist

str1 = "Emma-is-a-data-scientist"

lst = str1.split("-")

for i in lst:
    print(i)
