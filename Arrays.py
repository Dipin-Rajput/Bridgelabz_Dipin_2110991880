# Arrays

# Arrays is a data structure which store multiple elements of same type, in contiguous manner.
# Python does not actually contains arrays, but python list is used in the same way as an array.

# eg: 
 
my_array = [7, 12, 9, 11, 3]
print(my_array)

# Program to find the lowest value in an array

arr = [7, 12, 9, 11, 3]
minval = arr[0]


for i in arr:
    if(i < minval):
        minval = i

print("Lowest value:", minval)

# Program to find the greatest value in an array

arr = [7, 9, 5, 12, 3]
maxval = arr[0]

for i in arr:
    if(i > maxval):
        maxval = i

print("Greatest value:", maxval)

# Time Complexity of both algorithm is O(n), as loop iterates over, the whole length of list/array.
