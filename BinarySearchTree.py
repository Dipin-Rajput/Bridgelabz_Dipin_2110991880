# Binary Search Tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Adding nodes to BST

    def add(self, data):

        newnode = Node(data)

        if(self.root == None):
            self.root = newnode
        
        else:
            self._add_recursive(self.root, data)

    def _add_recursive(self, root, data):
    
        if(data < root.data):
            if(root.left == None):
                root.left = Node(data)

            else:
                self._add_recursive(root.left, data)

        else:
            if(root.right == None):
                root.right = Node(data)

            else:
                self._add_recursive(root.right, data)

    # Inorder Traversal

    def inorder(self):
        print("Inorder: ", end = "")
        def _inorder_recursive(node):

            if(node == None):
                return
            
            _inorder_recursive(node.left)
            print(node.data, end = " ")
            _inorder_recursive(node.right)

        _inorder_recursive(self.root)
        print()

    # Preorder Traversal

    def preorder(self):
        print("Preorder: ", end = "")
        def _preorder_recursive(node):

            if(node == None):
                return
            
            print(node.data, end = " ")
            _preorder_recursive(node.left)
            _preorder_recursive(node.right)

        _preorder_recursive(self.root)
        print()

    # Postorder Traversal

    def postorder(self):
        print("Postorder: ", end = "")
        def _postorder_recursive(node):

            if(node == None):
                return
            
            _postorder_recursive(node.left)
            _postorder_recursive(node.right)
            print(node.data, end = " ")

        _postorder_recursive(self.root)
        print()

# ---------------------------------------------------------------------------------------------------------------------------------------

bst = BinarySearchTree()

lst = [5, 8, 6, 7, 2, 3, 4, 1]

for i in lst:
    bst.add(i)

bst.inorder()
bst.preorder()
bst.postorder()
