# 2) Implement Stack using Queues

from collections import deque

class StackUsingQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, val):
        self.queue.append(val)

        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if(self.is_empty()):
            return "Stack is Empty"
        return self.queue.popleft()
    
    def top(self):
        if(self.is_empty()):
            return "Stack is Empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)
print("top ---->>>>", stack.top())
print("Element poped ---->>>>", stack.pop())
stack.is_empty()
print("top ---->>>>", stack.top())