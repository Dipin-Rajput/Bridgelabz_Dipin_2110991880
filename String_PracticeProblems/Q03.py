# 3) Append a new string in the middle of a given string.

# Given:

# s1 = "Ault"
# s2 = "Kelly"

# Expected Output: AuKellylt

s1 = "Ault"
s2 = "Kelly"

middle_idx = int(len(s1)/2)

new_str = s1[ : 2] + s2 + s1[2 : ]
print("New string is:", new_str)