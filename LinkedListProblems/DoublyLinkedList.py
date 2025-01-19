# Doubly Linked List

# Doubly Linked List is a type of linked list in which each node contains a data element and two links pointing to the next and previous node in the sequence. This allows for more efficient operations such as traversals, insertions, and deletions because it can be done in both direction.

# Implemented Methods

# Addition

# 1. add(): To add data at the end
# 2. addfirst(): To add data at the start
# 3. insert(): To insert data at particular index

# Deletion

# 1. removefirst(): To remove data from start
# 2. removelast(): To remove data from end
# 3. remove(): To remove data at particular index

# size(): To calculate the size of the linked list
# display(): To display the elements of the linked list

# ---------------------------------------------------------------------------------------------------------------------------------------

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # add: function to add data at the end

    def add(self, data):

        newnode = Node(data)

        if(self.head == None):
            self.head = newnode
            return
        
        curnode = self.head
        while(curnode.next != None):
            curnode = curnode.next

        curnode.next = newnode
        newnode.prev = curnode

    # addfirst: function to add data at the start

    def addfirst(self, data):

        newnode = Node(data)

        if(self.head == None):
            self.head = newnode
            return
        
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    # insert: function to add data at the index

    def insert(self, idx, data):

        newnode = Node(data)

        if(self.head == None or idx == 0):
            self.addfirst(data)

        elif(idx >= self.size()):
            print("********* Index Out of Range *********")

        else:
            count = 0
            curnode = self.head
            while(count < idx - 1):
                count += 1
                curnode = curnode.next

            newnode.next = curnode.next
            curnode.next.prev = newnode
            curnode.next = newnode
            newnode.prev = curnode

    # removefirst(): To remove data from start

    def removefirst(self):

        if(self.head == None):
            print("Linked List is Empty")
            return
        
        if(self.head.next == None):
            self.head = None
            return
        
        self.head = self.head.next
        self.head.prev = None

    # removelast(): To remove data from end

    def removelast(self):

        if(self.head == None):
            print("Linked List is Empty")
            return
        
        if(self.head.next == None):
            self.head = None
            return
        
        secondlast = self.head
        lastnode = self.head.next

        while(lastnode.next != None):
            secondlast = secondlast.next
            lastnode = lastnode.next

        secondlast.next = None

    # remove(): To remove data at particular index

    def remove(self, idx):

        if(self.head == None):
            print("Linked List is Empty")
            return
        
        if(idx == 0):
            self.removefirst()
        
        elif(idx >= self.size()):
            print("Index Out of Range")

        elif(idx == self.size()-1):
            self.removelast()
        
        else:
            count = 0
            prevnode = self.head
            curnode = self.head.next

            while(curnode != Node and count < idx - 1):
                curnode = curnode.next
                prevnode = prevnode.next
                count += 1

            curnode.next.prev = prevnode
            prevnode.next = prevnode.next.next

    # size(): To calculate the size of the linked list

    def size(self):

        if(self.head == None):
            print("Linked List is Empty")
            return
        
        curnode = self.head
        size = 0
        while(curnode != None):
            size += 1
            curnode = curnode.next

        return size
    
    # display(): To display the elements of the linked list

    def display(self):
        
        if(self.head == None):
            print("Linked List is Empty")
            return
        
        print("Original:", end = " ")

        curnode = self.head
        print("Head", end = " <--> ")
        while(curnode != None):
            if(curnode.next == None):
                tail = curnode
            print(curnode.data, end = " <--> ")

            curnode = curnode.next
        print("Tail")

        # Reverse Order

        print("Reverse:", end = " ")

        print("Tail", end = " <--> ")
        while(tail != None):
            print(tail.data, end = " <--> ")
            tail = tail.prev
        print("Head")

# ---------------------------------------------------------------------------------------------------------------------------------------

DLL = DoublyLinkedList()

lst = [1, 2, 3, 4, 5]

for i in lst:
    DLL.add(i)

DLL.addfirst(10)
DLL.insert(2, 50)
print("--->>>")
DLL.display()
DLL.removefirst()
DLL.removelast()
print("--->>>")
DLL.display()
DLL.remove(1)
print("--->>>")
DLL.display()