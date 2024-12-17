# List

# List is the datatype, it is collection of values.
# The elements of list are enclosed in square brackets.
# It consist of different datatypes.
# It is ordered.
# It is mutable.
# It can takes duplicate values.
# List '[]' empty list with only square brackets.

a = list()
print(a)
print(type(a))

a = [1,2,3,4,5]
b = [5,4,3,2,1]
print(a == b) # False, which shows list is ordered.

# List is mutable, so we can change it according to requirement.

a[0] = 11
a[4] = 55
print(a)

l = list("computer")
print(l) # ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r']

# We can traverse in list using for loop.

x = list("hello World")
print(x)
for i in x:
    print(i)

# Slicing is also possible in list.

a = ["My", "rollno", "is", 1880]
print(a)
print(a[-5::])
print(a[::-1]) # Reversing a list
print(a[0:len(a):2])

# Comparing list

print([1,2,3] < [4,5,6]) # True, because 4>1
print([1,2,4,5] < [1,2,3,4]) # False because 4>3

# Operations in list

# Concatenation

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)

# Replication

l1 = l1*2
print(l1)

# Membership operator in list

print(5 in l1)
print(3 not in l1)

# Built in Operations

# append

n = [1, 2, 3]
n.append(4) # Append a single item at the end of the list
print(n)

# If tried with multiple elements, it will result in error.

n.append([5,6,7]) # but sub-list with elements in possible to add.
print(n)

# extend

# To add multiple elements at the end of the list, but it will also takes only one argument.

n.extend([100,200,300])
print(n)

# insert

# Add element at particular index in the list

n.insert(0, 700)
print(n)

# Deletion Operations

# del(): It deletes the list and its whole structure from python.

del(n)
# print(n) # error

# remove(): It deletes the element by its value.

a = [1250, 210, 300, 170, 700]
a.remove(300)
print(a)

# pop(): It deletes the element by its index, if not provided then it deletes the last element form the list.

a.pop(0)
a.pop()
print(a)

# clear(): Remvoe all the elements from the list and return empty list.

a.clear()
print(a)



