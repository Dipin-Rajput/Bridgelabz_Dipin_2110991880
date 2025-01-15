# 3) Delete middle element of a stack

# Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any additional data structure.


# Input : Stack[] = [1, 2, 3, 4, 5]
# Output : Stack[] = [1, 2, 4, 5]


# Input : Stack[] = [1, 2, 3, 4, 5, 6]
# Output : Stack[] = [1, 2, 3, 5, 6]


stack = [1, 2, 3, 4, 5, 6]
temp = []

n = int(len(stack)/2)

while(len(stack)-1 > n):
    temp.append(stack.pop())

stack.pop()

while(len(temp) > 0):
    stack.append(temp.pop())

print("Stack after deleting middle element:", stack)




    