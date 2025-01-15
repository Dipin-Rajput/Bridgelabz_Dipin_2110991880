# Stack

#  A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
# In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.

# The functions associated with stack are:

# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

# Implementation of stack can be done in various ways:

# 1. list
# 2. Collection module

# Stack Implementation using list

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        return

    def pop(self):
        if self.isempty():
            return "Stack is Empty."
        return self.stack.pop()
        
    def peek(self):
        if self.isempty():
            return "Stack is Empty."
        return self.stack[-1]
    
    def isempty(self):
        if(len(self.stack) == 0):
            return True
        return False
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print("---->>>>", self.stack)
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("pop:", stack.pop())
stack.display()
print("top:", stack.peek())
print("empty?", stack.isempty())
print("size:", stack.size())

# The biggest issue is that it can run into speed issues as it grows. The items in the list are stored next to each other in memory, if the stack grows bigger than the block of memory that currently holds it, then Python needs to do some memory allocations. This can lead to some append() calls taking much longer than other ones.


# Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

# Stack Implementation using Collection Module

from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def size(self):
        if self.is_empty():
            return "Stack is Empty"
        return len(self.stack)
    
    def display(self):
        return self.stack
    
stack = Stack()

stack.push(2)
stack.push(1)
stack.push(3)
stack.push(7)
stack.push(4)
print("---->>>>", stack.display())
print(stack.pop())
print("---->>>>", stack.display())
print(stack.peek())
print(stack.size())


# Balanced Parentheses

str = "(()(())())"
stack = []

for i in str:

    if(not stack):
        stack.append(i)
        continue

    if(i == "("):
        stack.append(i)
    else:
        if(stack[-1] == "("):
            stack.pop()

if(len(stack) == 0):
    print("String has Balanced Parentheses:", str)

else:
    print("String doesn't has Balanced Parentheses:", str)


# Evaluate Postfix Expression using stack.

str = "53+82-*"
stack = []

for i in str:
    if(i.isdigit()):
        stack.append(i)

    else:
        val1 = int(stack.pop())
        val2 = int(stack.pop())

        match i:

            case "+": stack.append(val1 + val2)
            case "-": stack.append(val1 - val2)
            case "*": stack.append(val1 * val2)
            case "/": stack.append(int(val1 / val2))

print("Evaluation of Postfix Expression is:", stack.pop())