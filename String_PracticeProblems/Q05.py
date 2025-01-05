# 5) Arrange string characters such that lowercase letters should come first.

# Given: str1 = "PyNaTive"
# Expected Output: yaivePNT

str1 = "PyNaTive"
lower = ""
upper = ""

for i in str1:
    if(i.islower()):
        lower = lower + i
    else:
        upper = upper + i

print("New string is:", lower + upper)
