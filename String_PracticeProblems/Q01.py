# 1) Create a string made of the first, middle, and last character.

# Given: str1 = "James"
# Expected Output: Jms

str1 = "James"

middle = int(len(str1)/2)

print("String made of first, middle and last character:", str1[0] + str1[middle] + str1[-1])
