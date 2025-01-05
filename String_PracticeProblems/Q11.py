# 11) Write a program to count occurrences of all characters within a string.

# Given: str1 = "Apple"
# Expected Outcome: {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "Apple"
dict = {}

for i in str1:
    dict[i] = str1.count(i)

print("Occurences of all characters is:", dict)


