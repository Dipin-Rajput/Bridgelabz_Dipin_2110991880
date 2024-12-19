# Sets

# Set are the another datatype of python, it store elements inside curly braces.
# It is mutable in nature, which means you can append, del, insert in set.
# Set are unordered, because of this it does not take index.
# It cannot hold duplicates values.

# Set can store only hashable datatypes, which are immutable, such as int, float, strings, tuple, boolean and cannot store list, dict, sets.

a = {}
print(type(a)) # It will display <class 'dict'>, beacause sets and dictionary both are stored in curly braces.

# To create empty set

a = set()
print(type(a))

a = {10, 20, 30, 40, 50, 10}
print(a) # {50, 20, 40, 10, 30} because sets are unordered and it does not store duplicate values.

# Set Operations

# 1. add(): add the value to the set.

a.add(6)
print(a)

# 2.update(): update can be used to add multiple items.

b = [1, 2, 3] # or b = {4, 5} or b = (9, 8, 7)
a.update(b)
print(a)

# remove(): It removes the element by the value.

a.remove(10)
# a.remove(7) # but gives KeyError, if element does not exist.
print(a)

# discard(): It also removes the element by the value, but does not give error if element don't exist.

a.discard(7)
print(a)

# pop(): Because set is unordered it pop any element.

a.pop()
print(a)

# clear(): It removes all the elements form the set.

a.clear()
print(a)

# del(): It delets the whole structure of the set.

del(a)
# print(a) NameError: name 'a' is not defined

# Basic set Operations

# union() or |: It combine all the elements form both the sets.

a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a | b) # or x = a.union(b)

# intersection() or &: It returns the common element present in both sets.

print(a & b) # or x = a.intersection(b)

# difference or -: It returns only uncommon values.

print(a - b) # It returns the element only present in a.
print(b - a) # It returns the element only present in b.

# symmetric difference: It remove common values and print rest of the values.

print(a ^ b)

# To update the set without creating new variable and updation into existing sets, we use update with above operations.
# It works for intersection, difference and symmetric difference.

a.intersection_update(b) # put all the common elements of a and b in a.
print(a)

# set functions

a = {1, 2, 3}
b = {4, 1, 2, 3, 5, 6}

# isdisjoint(): If there is no common value in a and b it return true.

print(a.isdisjoint(b))

# issubset(): If all the values of a present in b, then it is a subset.

print(a.issubset(b))

# issuperset(): returns true if one set is big and all elements of b in a.

print(a.issuperset(b))