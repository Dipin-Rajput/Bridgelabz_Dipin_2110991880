# 7) Create a mixed string using the following rules.

# Given:

# s1 = "Abc"
# s2 = "Xyz"

# Expected Output: AzbycX

s1 = "Abcdef"
s2 = "Xyz"

lst = []

i = 0

while(i < len(s1) or i < len(s2)):

    if(i < len(s1)):
        lst.append(s1[i])

    if(i < len(s2)):
        lst.append(s2[len(s2) - i - 1])

    i += 1

s3 = "".join(lst)

print("New string is:", s3)