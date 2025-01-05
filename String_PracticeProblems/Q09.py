# 9) Find all occurrences of a substring in a given string by ignoring the case.

# Given: 

# str1 = "Welcome to USA. usa awesome, isn't it?"

# Expected Outcome: 

# The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"
temp = str1.lower()

print("Number of occurence of 'USA' in string is:", temp.count("usa"))
