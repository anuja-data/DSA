class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # Push Operation
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # # Pop Operation
    # def pop(self):
    #     if self.isempty():
    #         print("Stack is Empty")
    #     else:
    #         temp = self.top
    #         print("Popped Element:", temp.data)
    #         self.top = self.top.next
    #         temp = None

    # # Display Operation
    # def display(self):
    #     if self.isempty():
    #         print("Stack is Empty")
    #     else:
    #         print("Stack Contents....")
    #         temp = self.top
    #         while temp:
    #             print(temp.data)
    #             temp = temp.next

    # # Reverse String Using Stack
    # def reverse_string(self, string):
    #     temp = []
    #     for ch in string:
    #         temp.append(ch)

    #     reverse = ""
    #     while len(temp) > 0:
    #         reverse += temp.pop()

    #     print("Reversed String:", reverse)

    # # Reverse Stack Using Another Stack
    # def reverse_stack(self):
    #     temp_stack = stack()

    #     while not self.isempty():
    #         temp = self.top
    #         self.top = self.top.next
    #         temp.next = None
    #         temp_stack.push(temp)

    #     self.top = temp_stack.top
    #     print("Reversed Stack:")
    #     self.display()


# Main Program

st = stack()

# Push Elements
st.push(Node(59))
st.push(Node(24))
st.push(Node(33))
st.push(Node(89))
st.push(Node(90))

st.print()
# # Display Stack
# st.display()

# # Pop Elements
# st.pop()
# st.pop()

# # Display After Pop
# st.display()

# # Reverse String
# st.reverse_string("NANDINI")

# # Reverse Stack
# st.reverse_stack()