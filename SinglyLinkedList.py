# Singly Linked List

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

class SinglyLinkedList:

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

    # addfirst: function to add data at the start

    def addfirst(self, data):

        newnode = Node(data)

        if(self.head == None):
            self.head = newnode
            return
        
        newnode.next = self.head
        self.head = newnode

    # insert: function to add data at the index

    def insert(self, idx, data):

        if(idx == 0):
            self.addfirst(data)
            return
        
        if(idx >= self.size()):
            print("Index Out of Range")
            return

        newnode = Node(data)
        count = 0

        curnode = self.head

        while(count != idx - 1):
            count += 1
            curnode = curnode.next

        newnode.next = curnode.next
        curnode.next = newnode

    # removefirst(): To remove data from start

    def removefirst(self):

        if(self.head == None):
            print("List is empty.")
            return
        
        self.head = self.head.next

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
            lastnode = lastnode.next
            secondlast = secondlast.next

        secondlast.next = None

    # remove(): To remove data at particular index

    def remove(self, idx):

        if(self.head == None):
            print("List is Empty")
            return

        prev = self.head
        curnode = self.head.next

        count = 0

        while(curnode != None and count < idx - 1):
            curnode = curnode.next
            prev = prev.next
            count += 1

        prev.next = prev.next.next

    # size(): To calculate the size of the linked list
    
    def size(self):

        curnode = self.head
        size = 0
        while(curnode != None):
            size += 1
            curnode = curnode.next

        return size
    
    # display(): To display the elements of the linked list

    def display(self):

        curnode = self.head
        print("Head ->", end = " ")

        while(curnode is not None):
            print(curnode.data, "->", end = " ")
            curnode = curnode.next

        print("Tail")

SLL = SinglyLinkedList()

lst = [1, 2, 3, 4, 5]

for i in lst:
    SLL.add(i)

SLL.addfirst(10)
SLL.insert(1, 20)
print("--->>>", end = " ")
SLL.display()
SLL.removefirst()
SLL.removelast()
SLL.remove(3)
print("--->>>", end = " ")
SLL.display()
print("--->>> Size:", SLL.size())