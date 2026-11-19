class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert (self,new_node):
        if self.root is None: #creating the root node
            self.root= new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                elif new_node.data >= temp.data:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

def postorder(temp): #recursive
    if temp is None:
        return
    else:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data,end=" ")
btree=BST()
btree.insert(Node(10))
btree.insert(Node(15))
btree.insert(Node(12))
btree.insert(Node(40))
btree.insert(Node(19))
btree.insert(Node(80))
postorder(btree.root)