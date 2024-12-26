# Tuple

# Tuple are another sequence data-type that is similar to list.
# A tuple consist of values seperated by commas and it is enclosed in parethesis.
# Tuples are immutable data-types, we cannot perform add, update and delete operation.
# Tuples are ordered.
# It can have duplicate values.

# Creating tuples using assignment operator with parenthesis. 

a = (1,2,3,4,5)
print(a)

# Creating tuples with tuple() function.

t = tuple(["apple", "bannana", 1880])
print(type(t))

# Creating tuples using user input.

# t = tuple()
# n = int(input("Enter the size: "))
# for i in range (n):
#     a = input("Enter number: ")
#     t = t + (a,)
# print("Output is: ")
# print(t)

# Nested tuples

a = (1, 2, "Hello")
b = ("World", 3, 4)
c = (a, b)
print(c)

# Traversing and Slicing in tuples reamin same as other.

tup = (1, 2, 3)
for i in range(len(tup)):
    print(tup[i])

print(tup[::-2])

# Packing and Unpacking in tuple.

a = 1, 2, 3, 4, 5 # packing
(aa, ab, ac, ad, ae) = a # unpacking
print(aa, ab, ac, ad, ae)

(aa, bb, *cc) = a
print(aa, bb, cc)

(aa, *bb, cc) = a
print(aa, bb, cc)

# Common tuple Operations

# 1. Concatenation

x = 1, 2, 3
y = 5, 4, 6
z = x + y
print(z)

# 2. Repetition/ Multiplication

x = 1, 2, 3, 4
y = x * 2
print(y)

# 3. Membership operator (in and not in)

print(4 in x)
print(7 not in x)

# Tuple functions

# 1. len()

n = (1, 2, 3, 4, 3, 2, 3, 3)
print(len(n))

# 2. count(): It count the occurence of an item in tuple.

print(n.count(3))

# 3. index(): print the index of first occurence of the element.

print(n.index(2))

# 4. any(): print true if a tuple is having at least one item, if its empty return false.

print(any(n))

#  5. max() and min(): print the maximum and minimum element form the tuple.
# It is not supported if tuple contains string and integer datatype.

print(max(n))
print(min(n))

y = ("Apple", "cherry", "peach")

print(max(y)) # output: peach
print(min(y)) # output: Apple

# 6. sorted(): It is used to sort the element of a tuple, It returns the list after sorting.

print(sorted(n))

# Deletion Operation in tuple: you cannot perform, remove, pop, clear operations in tuple, you can only delete the whole structure of the tuple.

# del(): del() function is used to delete a tuple.

del(y)
# print(y) # Error: as y is deleted from the python.
