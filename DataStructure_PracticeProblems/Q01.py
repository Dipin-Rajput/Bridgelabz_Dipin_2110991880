# 1) Create a list by picking an odd-index items from the first list and even index items from the second.

# Given:

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]

# Expected Output:

# Element at odd-index positions from list one [6, 12, 18]
# Element at even-index positions from list two [4, 12, 20, 28]
# Printing Final third list [6, 12, 18, 4, 12, 20, 28]

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28, 54, 98]

odd = []
even = []
i = 0

while(i < len(l1) or i < len(l2)):
    if(i < len(l1) and i % 2 != 0):
        odd.append(l1[i])

    if(i < len(l2) and i % 2 == 0):
        even.append(l2[i])
    
    i += 1

l3 = odd + even

print("Element at odd-index from list one:", odd)
print("Element at even-index from list one:", even)
print("Final third list:", l3)