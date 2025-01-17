# Linked List

# It is a list, where the nodes are linked together. Each nod e contains data and a pointer.
# It is linked in a way that each node points to where in the memory where the next noded is placed.
# It consist of node with some sort of data, and a pointer, or link to the next node.
# Nodes are stored where ever is free space present in the memory.

#  --------         --------         --------         -------
#  | data |     --> | data |     --> | data |     --> | data |
#  --------  __/    --------  __/    --------  __/    --------
#  | next | /       | next | /       | next | /       | next |
#  --------         --------         --------         --------
#  Head Node                                          Tail Node

# Time Complexity in Linked list

# Access                  |   O(n)
# Search                  |   O(n)
# Insertion (Start)       |   O(1)
# Insertion (At index)    |   O(n)
# Insertion (end)         |   O(1)
# Deletion (Start)        |   O(1)
# Deletion (At index)     |   O(n)
# Deletion (end)          |   O(n)
# Space Complexity        |   O(n)

# Types of Linked List

# 1. Singly Linked List
# 2. Doubly Linked List
# 3. Circular Linked List

# Real World Examples

# 1. Previous and next in a web browser
# 2. Music Player
# 3. File System

# ---------------------------------------------------------------------------------------------------------------------------------------

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        
        newnode = Node(data)

        if(self.head == None):
            self.head = newnode
            return
        
        curnode = self.head
        while(curnode.next != None):
            curnode = curnode.next

        curnode.next = newnode

    def remove(self):

        if(self.head == None):
            print("Linked List is Empty.")
            return
        
        secondlast = self.head
        lastnode = self.head.next

        while(lastnode.next != None):
            secondlast = secondlast.next
            lastnode = lastnode.next

        secondlast.next = None

    def display(self):

        if(self.head == None):
            print("Linked List is Empty.")
            return
        
        print("Head", end = " --> ")
        curnode = self.head
        while(curnode != None):
            print(curnode.data, end = " --> ")
            curnode = curnode.next

        print("Tail")

List = LinkedList()

lst = [1, 2, 3, 4, 5]

for i in lst:
    List.add(i)

List.remove()
List.display()