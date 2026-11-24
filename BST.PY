# NODE CLASS
class Node:
    def __init__(self, data):
        self.data = data       # Store node value
        self.left = None       # Left child
        self.right = None      # Right child

# BINARY SEARCH TREE CLASS

class BST:

    def __init__(self):
        self.root = None       # Initially tree is empty


   
    # 1. INSERT OPERATION
  

    def insert(self, root, data):

        # If current position is empty, create new node
        if root is None:
            return Node(data)

        # If data is smaller, insert into left subtree
        if data < root.data:
            root.left = self.insert(root.left, data)

        # If data is greater, insert into right subtree
        elif data > root.data:
            root.right = self.insert(root.right, data)

        # Return the unchanged/current root node
        return root


   
    # 2. SEARCH OPERATION
   

    def search(self, root, key):

        # If node is None, element is not present
        if root is None:
            return False

        # If current node matches the key, element is found
        if root.data == key:
            return True

        # If key is smaller, search in left subtree
        if key < root.data:
            return self.search(root.left, key)

        # Otherwise search in right subtree
        return self.search(root.right, key)


    
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



    # 4. PREORDER TRAVERSAL
    # Order: ROOT -> LEFT -> RIGHT
   

    def preorder(self, root):

        if root is not None:

            # First print root node
            print(root.data, end=" ")

            # Then visit left subtree
            self.preorder(root.left)

            # Finally visit right subtree
            self.preorder(root.right)


    # 5. POSTORDER TRAVERSAL
    # Order: LEFT -> RIGHT -> ROOT
   

    def postorder(self, root):

        if root is not None:

            # First visit left subtree
            self.postorder(root.left)

            # Then visit right subtree
            self.postorder(root.right)

            # Finally print root node
            print(root.data, end=" ")


    
    # 6. FIND MINIMUM VALUE
   

    def find_min(self, root):

        # If tree is empty, return None
        if root is None:
            return None

        # Minimum value is present at leftmost node
        while root.left is not None:
            root = root.left

        # Return minimum value
        return root.data


   
    # 7. FIND MAXIMUM VALUE
  

    def find_max(self, root):

        # If tree is empty, return None
        if root is None:
            return None

        # Maximum value is present at rightmost node
        while root.right is not None:
            root = root.right

        # Return maximum value
        return root.data


    # 8. DELETE OPERATION
   

    def delete(self, root, key):

        # If node does not exist, return None
        if root is None:
            return None

        # If key is smaller, search in left subtree
        if key < root.data:
            root.left = self.delete(root.left, key)

        # If key is greater, search in right subtree
        elif key > root.data:
            root.right = self.delete(root.right, key)

        # If key matches, delete this node
        else:

            # CASE 1: Node has no children (leaf node)
            if root.left is None and root.right is None:
                return None

            # CASE 2: Node has only right child
            elif root.left is None:
                return root.right

            # CASE 2: Node has only left child
            elif root.right is None:
                return root.left

            # CASE 3: Node has two children
            else:

                # Find minimum value in right subtree
                min_value = self.find_min(root.right)

                # Replace current node value with minimum value
                root.data = min_value

                # Delete the duplicate minimum node
                root.right = self.delete(root.right, min_value)

        # Return updated root
        return root


    # 9. COUNT TOTAL NODES
  

    def count_nodes(self, root):

        # Empty tree contains zero nodes
        if root is None:
            return 0

        # Count current node + left subtree + right subtree
        return (1 +
                self.count_nodes(root.left) +
                self.count_nodes(root.right))

    # 10. COUNT LEAF NODES


    def count_leaf_nodes(self, root):

        # Empty tree has zero leaf nodes
        if root is None:
            return 0

        # Leaf node has no left and no right child
        if root.left is None and root.right is None:
            return 1

        # Count leaf nodes in both subtrees
        return (self.count_leaf_nodes(root.left) +
                self.count_leaf_nodes(root.right))


  
    # 11. COUNT NON-LEAF NODES
    

    def count_non_leaf_nodes(self, root):

        # Empty tree has zero non-leaf nodes
        if root is None:
            return 0

        # If node has no children, it is a leaf
        if root.left is None and root.right is None:
            return 0

        # Count current non-leaf node + both subtrees
        return (1 +
                self.count_non_leaf_nodes(root.left) +
                self.count_non_leaf_nodes(root.right))


    # 12. HEIGHT OF BST
   

    def height(self, root):

        # Empty tree has height -1
        if root is None:
            return -1

        # Calculate height of left subtree
        left_height = self.height(root.left)

        # Calculate height of right subtree
        right_height = self.height(root.right)

        # Return maximum height + 1 for current node
        return 1 + max(left_height, right_height)


  
    # 13. SUM OF ALL NODES
   

    def sum_nodes(self, root):

        # Empty tree has sum zero
        if root is None:
            return 0

        # Add current node + left subtree sum + right subtree sum
        return (root.data +
                self.sum_nodes(root.left) +
                self.sum_nodes(root.right))



# MAIN PROGRAM


# Create BST object
bst = BST()

# Elements to insert into BST
values = [50, 30, 70, 20, 40, 60, 80]

# Insert all elements one by one
for value in values:
    bst.root = bst.insert(bst.root, value)



# DISPLAY TRAVERSALS


print("Inorder Traversal:")
bst.inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)



# SEARCH ELEMENT


key = 40

if bst.search(bst.root, key):
    print("\nElement Found")
else:
    print("\nElement Not Found")



# FIND MINIMUM AND MAXIMUM


print("Minimum Value:", bst.find_min(bst.root))
print("Maximum Value:", bst.find_max(bst.root))


# COUNT NODES


print("Total Nodes:", bst.count_nodes(bst.root))

print("Leaf Nodes:", bst.count_leaf_nodes(bst.root))

print("Non-Leaf Nodes:", bst.count_non_leaf_nodes(bst.root))



# HEIGHT OF BST


print("Height of BST:", bst.height(bst.root))


# SUM OF ALL NODES


print("Sum of All Nodes:", bst.sum_nodes(bst.root))

# DELETE ELEMENT

bst.root = bst.delete(bst.root, 70)

print("Inorder After Deletion:")
bst.inorder(bst.root)

print()  # Move cursor to next line
