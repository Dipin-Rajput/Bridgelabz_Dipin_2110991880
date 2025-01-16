# Queue

# Like a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first.
# The queue has the two ends front and rear. The next element is inserted from the rear end and removed from the front end.

# Operations associated with queue are: 

# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
# Front: Get the front item from queue – Time Complexity : O(1)
# Rear: Get the last item from queue – Time Complexity : O(1)

# Implementation of Queue can be done in various ways:

# 1. List
# 2. deque from collection module
# 3. Queue form queue module

# -----------------------------------------------------------------------------------------------------------------------------------------

# Queue implementation using list

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    
    def display(self):
        return self.queue
    
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("----->>>>>", queue.display())
queue.dequeue()
queue.dequeue()
print("----->>>>>", queue.display())
queue.enqueue(4)
queue.enqueue(5)
print("----->>>>>", queue.display())
print("Front:", queue.front())
print("Rear:", queue.rear())

# -----------------------------------------------------------------------------------------------------------------------------------------

# Queue implementation using Collections.deque

from collections import deque

class Collection_Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.popleft()

    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    
    def display(self):
        return self.queue
    
queue = Collection_Queue()

queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
print("----->>>>>", queue.display())
queue.dequeue()
queue.dequeue()
print("----->>>>>", queue.display())
queue.enqueue(9)
queue.enqueue(10)
print("----->>>>>", queue.display())
print("Front:", queue.front())
print("Rear:", queue.rear())

# -----------------------------------------------------------------------------------------------------------------------------------------

# Queue implementation using queue.Queue

from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)
print(q)
q.get()
q.get()
q.put(4)
q.put(5)
q.put(7)
print(q.empty())
print(q.full())
print(q.qsize())

for i in q.queue:
    print(i, end = " ")