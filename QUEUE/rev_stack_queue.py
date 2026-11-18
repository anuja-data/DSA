
class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return None
        else:
            temp = self.top
            popped_data = temp.data
            print("popped Element:", temp.data)
            self.top = self.top.next
            temp = None
            return popped_data

    def print(self):
        if self.isempty():
            print("stack is empty")
        else:
            print("stack contains...")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    # Reverse stack using queue
    def reverse_stack(self):
        q1 = LQueue()

        while not self.isempty():
            q1.enqueue(Node(self.pop()))

        while q1.front:
            self.push(Node(q1.dequeue()))


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.isempty():
            print("queue is empty")
            return None
        else:
            temp = self.front
            deleted_data = temp.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            temp = None
            return deleted_data

    def print(self):
        if self.isempty():
            print("queue is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    # Reverse queue using stack
    def reverse_queue(self):
        s1 = stack()

        while not self.isempty():
            s1.push(Node(self.dequeue()))

        while not s1.isempty():
            self.enqueue(Node(s1.pop()))


# Main program

# Reverse stack using queue
s = stack()

s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))

print("Original Stack:")
s.print()

print("\nReverse Stack using Queue:")
s.reverse_stack()
s.print()


# Reverse queue using stack
que = LQueue()

que.enqueue(Node(23))
que.enqueue(Node(75))
que.enqueue(Node(28))
que.enqueue(Node(93))

print("\nOriginal Queue:")
que.print()

print("\nReverse Queue using Stack:")
que.reverse_queue()
que.print()
