# 2) Create a string made of the middle three characters.

# Given:

# Case 1: str1 = "JhonDipPeta"
# Output: Dip

# Case 2: str2 = "JaSonAy"
# Output: Son

str1 = "JhonDipPeta"

middle_idx1 = int(len(str1)/2)
print("String with middle three charaters:", str1[middle_idx1 - 1] + str1[middle_idx1] + str1[middle_idx1 + 1])

str2 = "JaSonAy"

middle_idx2 = int(len(str2)/2)
print("String with middle three charaters:", str2[middle_idx2 - 1] + str2[middle_idx2] + str2[middle_idx2 + 1])