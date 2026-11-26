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
    
# 3. INORDER TRAVERSAL
    # Order: LEFT -> ROOT -> RIGHT
  

    def inorder(self, root):

        # Check whether current node exists
        if root is not None:

            # First visit left subtree
            self.inorder(root.left)

            # Then print root node
            print(root.data, end=" ")

            # Finally visit right subtree
            self.inorder(root.right)

    def level_order(self,root):
        if root is  None:
            print("BST is empty")
            return
        arr=[]
        cont=0  #for counting visited Node
        level=0
        arr.append(root)
        while cont<len(arr):
            node_count=len(arr)-cont
            print("\n Level:",level,end=" ")
            for i in range(node_count):
                temp=arr[cont]
                cont+=1
                print(temp.data,end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level+=1
        print("\nHeight of the tree:",level-1)

bst = BST()

# Elements to insert into BST
values = [50, 30, 70, 20, 40, 60, 80]

# Insert all elements one by one
for value in values:
    bst.root = bst.insert(bst.root, value)

print("Inorder Traversal:")
bst.inorder(bst.root)


print("\nLevel Order Traversal:")
bst.level_order(bst.root)


