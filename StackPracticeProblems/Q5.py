# 5) Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.

# Note: If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.

# Examples:

# Input : arr = [2, 1, 8]
# Output : 1
# Left smaller LS = [0, 0, 1]
# Right smaller RS = [1, 0, 0]
# Maximum Diff of abs(LS[i] - RS[i]) = 1

# Input : arr = [2, 4, 8, 7, 7, 9, 3]
# Output : 4
# Left smaller LS = [0, 2, 4, 4, 4, 7, 2]
# Right smaller RS = [0, 3, 7, 3, 3, 3, 0]
# Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4

# Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
# Output : 1

arr = [2, 1, 8]
LS = [0] * len(arr)
RS = [0] * len(arr)

stack1 = []
stack2 = []

for i in range(len(arr)):
    while(stack1 and stack1[-1] >= arr[i] ):
        stack1.pop()

    if stack1:
        LS[i] = stack1[-1]

    stack1.append(arr[i])

for i in range(len(arr)-1, -1, -1):
    while(stack2 and stack2[-1] >= arr[i]):
        stack2.pop()

    if stack2:
        RS[i] = stack2[-1]

    stack2.append(arr[i])

max = 0

for i in range(len(arr)):
    diff = abs(LS[i] - RS[i])
    if(diff > max):
        max = diff

print("Maximum Abolute difference is:", max)