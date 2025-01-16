# 1) Reversing the first K elements of a Queue

# Given an integer k and a queue of integers, The task is to reverse the order of the first k elements of the queue, leaving the other elements in the same relative order.

# Only following standard operations are allowed on queue.

# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.

# -----------------------------------------------------------------------------------------------------------------------------------------

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]

    def display(self):
        return self.queue

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

queue = Queue()

for i in arr:
    queue.enqueue(i)

print("Queue before operation:", queue.display())

k = 5
stack = []

while(k > 0):
    stack.append(queue.dequeue())
    k -= 1

rem_len = queue.size()

while(len(stack) > 0):
    queue.enqueue(stack.pop())

while(rem_len > 0):
    queue.enqueue(queue.dequeue())
    rem_len -= 1

print("Resulting Queue:", queue.display())