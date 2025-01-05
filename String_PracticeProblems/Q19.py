# 19) Replace each special symbol with # in the following string.

# Given: str1 = "/*Jon is @developer & musician!!"
# Expected Output: ##Jon is #developer # musician##

str1 = "/*Jon is @developer & musician!!"

maptable = str.maketrans("/*@&!", "#####")
print("Output is:", str1.translate(maptable))