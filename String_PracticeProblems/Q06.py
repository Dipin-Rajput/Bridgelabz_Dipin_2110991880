# 6) Count all letters, digits, and special symbols from a given string.

# Given: str1 = "P@#yn26at^&i5ve"

# Expected Outcome:
 
# Chars = 8
# Digits = 3
# Symbol = 4


str1 = "P@#yn26at^&i5ve"

letters = 0
digits = 0
special = 0

for i in str1:
    if(i.isalpha()):
        letters += 1

    elif(i.isdigit()):
        digits += 1
    
    else:
        special += 1

print(f"Number of letters in string is: {letters}")
print(f"Number of digits in string is: {digits}")
print(f"Number of special symbol in string is: {special}")