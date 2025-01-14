# Stack

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