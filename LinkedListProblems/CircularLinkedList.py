# Circular Linked List

# A Circular Linked List is a variation of the standard linked list. In a standard linked list, the last element points to null, indicating the end of the list. However, in a circular linked list, the last element points back to the first element, forming a loop

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

class CircularLinkedList:

    def __init__(self):
        self.head = None

    # add(): To add data at the end

    def add(self, data):

        newnode = Node(data)

        if(self.head == None):
            newnode.next = newnode
            self.head = newnode
            return
        
        curnode = self.head
        while(curnode.next != self.head):
            curnode = curnode.next

        curnode.next = newnode
        newnode.next = self.head

    # addfirst(): To add data at the start

    def addfirst(self, data):

        newnode = Node(data)

        if(self.head == None):
            newnode.next = newnode
            self.head = newnode
            return

        curnode = self.head
        while(curnode.next != self.head):
            curnode = curnode.next

        curnode.next = newnode
        newnode.next = self.head
        self.head = newnode

    # insert(): To insert data at particular index

    def insert(self, idx, data):

        newnode = Node(data)

        if(self.head == None or idx == 0):
            self.addfirst(data)
        
        elif(self.size() >= idx):
            print("Index Out of Range")

        else:
            curnode = self.head
            count = 0
            while(count < idx - 1):
                count += 1
                curnode = curnode.next

            newnode.next = curnode.next
            curnode.next = newnode

    # removefirst(): To remove data from start

    def removefirst(self):

        if(self.head == None):
            print("Linked List is Empty")
            return
        
        curnode = self.head
        while(curnode.next != self.head):
            curnode = curnode.next

        curnode.next = curnode.next.next
        self.head = self.head.next

    # removelast(): To remove data from end

    def removelast(self):

        if(self.head == None):
            print("Linked List is Empty")
            return
        
        secondlast = self.head
        lastnode = self.head.next

        while(lastnode.next != self.head):
            secondlast = secondlast.next
            lastnode = lastnode.next

        secondlast.next = self.head

    # remove(): To remove data at particular index

    def remove(self, idx):

        if(self.head == None):
            print("Linked List is Empty")
            
        elif(idx == 0):
            self.removefirst()

        elif(idx == self.size() - 1):
            self.removelast()

        else:
            secondlast = self.head
            lastnode = self.head.next
            count = 0

            while(count < idx - 1):
                count += 1
                secondlast = secondlast.next
                lastnode = lastnode.next
            
            secondlast.next = secondlast.next.next

    # size(): To calculate the size of the linked list

    def size(self):

        if(self.head == None):
            print("Linked List is Empty")
            return
        
        curnode = self.head
        size = 0
        while(curnode != self.head):
            size += 1
            curnode = curnode.next

        return size
    
    # display(): To display the elements of the linked list

    def display(self):

        curnode = self.head

        while(curnode.next != self.head):
            print(curnode.data, end = " -> ")
            curnode = curnode.next
        print(curnode.data)

# ---------------------------------------------------------------------------------------------------------------------------------------

CLL = CircularLinkedList()

lst = [1, 2, 3, 4, 5]

for i in lst:
    CLL.add(i)

CLL.addfirst(10)
CLL.insert(4, 50)
print("--->>>", end = " ")
CLL.display()
CLL.remove(2)
print("--->>>", end = " ")
CLL.display()
CLL.removefirst()
CLL.removelast()
print("--->>>", end = " ")
CLL.display()

    