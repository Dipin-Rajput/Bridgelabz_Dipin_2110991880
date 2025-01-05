# 17) Remove all characters from a string except integers.

# Given: str1 = "I am 25 years and 10 months old"
# Expected Output: 2510

str1 = "I am 25 years and 10 months old"
lst = str1.split()
num = ""

for i in lst:
    if(i.isdigit()):
        num = num + i

print("Numbers from string are:", num)
