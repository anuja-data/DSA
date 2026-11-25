# # 1.leaf Node 
# # 2.node with right child 
# # 3.node with left child 
# # 4.node with both left and right children (node--iorder successor)

# # NODE CLASS
# class Node:
#     def __init__(self, data):
#         self.data = data       # Store node value
#         self.left = None       # Left child
#         self.right = None      # Right child

# # BINARY SEARCH TREE CLASS

# class BST:

#     def __init__(self):
#         self.root = None       # Initially tree is empty


   
#     # 1. INSERT OPERATION
  

#     def insert(self, root, data):

#         # If current position is empty, create new node
#         if root is None:
#             return Node(data)

#         # If data is smaller, insert into left subtree
#         if data < root.data:
#             root.left = self.insert(root.left, data)

#         # If data is greater, insert into right subtree
#         elif data > root.data:
#             root.right = self.insert(root.right, data)

#         # Return the unchanged/current root node
#         return root

#     def del_node(self,root,value):
#         if root is None:
#             return 
#         if  value < root.data:
#             root.left=self.del_node(root.self,value)
#         elif value>root.data:
#             root.right=self.del_node(root.right,value)
#         else:
#             if root.left is None: #node with right child only
#                 return root.right
#             if root.right is None: #node with left child only
#                 return root.left 
#             # node has both left and right children
#             succ=self.get_successor(root)
#             root.data=succ.data
#             root.right=self.del_node(root.right,succ.data)
#             return root

#         def get_successor(self,temp):
#             temp=temp.right
#             while temp.left is not None and temp:

#     def inorder(self, root):
    
#             # Check whether current node exists
#             if root is not None:
    
#                 # First visit left subtree
#                 self.inorder(root.left)
    
#                 # Then print root node
#                 print(root.data, end=" ")
    
#                 # Finally visit right subtree
#                 self.inorder(root.right)
    

# # Create BST object
# bst = BST()

# # Elements to insert into BST
# values = [50, 30, 70, 20, 40, 60, 80]

# # Insert all elements one by one
# for value in values:
#     bst.root = bst.insert(bst.root, value)




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

    # FIND INORDER SUCCESSOR
    def get_successor(self, temp):

        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp

    # DELETE OPERATION
    def del_node(self, root, value):

        if root is None:
            return None

        if value < root.data:
            root.left = self.del_node(root.left, value)

        elif value > root.data:
            root.right = self.del_node(root.right, value)

        else:

            # CASE 1 AND 2:
            # No left child (leaf or right child only)
            if root.left is None:
                return root.right

            # CASE 3:
            # Only left child
            elif root.right is None:
                return root.left

            # CASE 4:
            # Both left and right children
            succ = self.get_successor(root)

            root.data = succ.data

            root.right = self.del_node(root.right, succ.data)

        return root
    
        # INORDER TRAVERSAL
    def inorder(self, root):

        if root is not None:

            self.inorder(root.left)

            print(root.data, end=" ")

            self.inorder(root.right)


# CREATE BST OBJECT
bst = BST()

# INSERT ELEMENTS ONE BY ONE
bst.root = bst.insert(bst.root, 50)
bst.root = bst.insert(bst.root, 30)
bst.root = bst.insert(bst.root, 70)
bst.root = bst.insert(bst.root, 20)
bst.root = bst.insert(bst.root, 40)
bst.root = bst.insert(bst.root, 60)
bst.root = bst.insert(bst.root, 80)

# BEFORE DELETION
print("Before deletion:")
bst.inorder(bst.root)

# DELETE NODE 50
bst.root = bst.del_node(bst.root, 50)

# AFTER DELETION
print("\nAfter deletion:")
bst.inorder(bst.root)