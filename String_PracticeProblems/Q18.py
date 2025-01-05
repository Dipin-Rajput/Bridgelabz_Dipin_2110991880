# 18) Find words with both alphabets and numbers.

# Given: str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output: Emma25 scientist50

str1 = "Emma25 is Data scientist50 and AI Expert"

lst = str1.split()

for i in lst:
    if(any(char.isalpha() for char in i) and any(char.isdigit() for char in i)):
        print(i, end = " ")