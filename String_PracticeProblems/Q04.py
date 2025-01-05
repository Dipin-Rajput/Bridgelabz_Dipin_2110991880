# 4) Create a new string made of the first, middle, and last characters of each input string.

# Given:

# s1 = "America"
# s2 = "Japan"

# Expected Output: AJrpan

s1 = "America"
s2 = "Japan"

middle1 = int(len(s1)/2)
middle2 = int(len(s2)/2)

newstr = s1[0] + s2[0] + s1[middle1] + s2[middle2] + s1[-1] + s2[-1]
print("New string is:", newstr)

