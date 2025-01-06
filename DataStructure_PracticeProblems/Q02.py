# 2) Remove and add item in a list.

# Given:
# list1 = [54, 44, 27, 79, 91, 41]

# Expected Output:

# List After removing element at index 4 [54, 44, 27, 79, 41]
# List after Adding element at index 2 [54, 44, 91, 27, 79, 41]
# List after Adding element at last [54, 44, 91, 27, 79, 41, 91]

list1 = [54, 44, 27, 79, 91, 41]

x = list1.pop(4)
print("List After removing element at index 4:", list1)

list1.insert(2, x)
print("List After adding element at index 2:", list1)

list1.append(x)
print("List After adding element at last:", list1)