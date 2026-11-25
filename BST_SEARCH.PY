# NODE CLASS
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BINARY SEARCH TREE CLASS
class BST:

    def __init__(self):
        self.root = None

    # INSERT OPERATION
    def insert(self, root, data):

        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # SEARCH OPERATION
    def search(self, root, value):

        if root is None:
            return None

        if root.data == value:
            return root

        elif value < root.data:
            return self.search(root.left, value)

        else:
            return self.search(root.right, value)

    # INORDER TRAVERSAL
    def inorder(self, root):

        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# CREATE BST OBJECT
bst = BST()

# INSERT ELEMENTS
bst.root = bst.insert(bst.root, 50)
bst.root = bst.insert(bst.root, 30)
bst.root = bst.insert(bst.root, 70)
bst.root = bst.insert(bst.root, 20)
bst.root = bst.insert(bst.root, 40)
bst.root = bst.insert(bst.root, 60)
bst.root = bst.insert(bst.root, 80)


# DISPLAY BST
print("BST Elements:")
bst.inorder(bst.root)


# SEARCH OPERATION
key = 40

result = bst.search(bst.root, key)

if result is not None:
    print(f"\nNode {key} found in BST!")
else:
    print(f"\nNode {key} not found in BST!")
