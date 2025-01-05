# 8) String characters balance test.

# Given:

# Case 1: 

# s1 = "Yn"
# s2 = "PYnative"
# Expected Output: True

# Case 2:

# s1 = "Ynf"
# s2 = "PYnative"
# Expected Output: False

s1 = "Yn"
s2 = "PYnative"
flag = 0

for i in s1:
    if(i not in s2):
        print("False")
        break
else:
    print("True")

s1 = "Ynf"
s2 = "PYnative"

for i in s1:
    if(i not in s2):
        print("False")
        break
else:
    print("True")