# 2)  Delete consecutive same words in a sequence

# Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.

# Examples:

# Input : ab aa aa bcd ab
# Output : 3

# As aa, aa destroys each other so,
# ab bcd ab is the new sequence.


# Input : tom jerry jerry tom
# Output : 0

# As first both jerry will destroy each other.
# Then sequence will be tom, tom they will also destroy
# each other. So, the final sequence doesn’t contain any
# word.

arr = ["ab", "aa", "aa", "bcd", "ab"]
stack = []

for i in arr:
    if stack and stack[-1] == i:
        stack.pop()

    else:
        stack.append(i)

print("The new sequence is:", stack)



