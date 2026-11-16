class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):

        if self.front is None:
            self.front = new_node
            return

        # Insert at first position
        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        # Insert at appropriate position
        temp = self.front

        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Create Priority Queue
pq = PriorityQueue()

pq.enqueue(node(100, 5))
pq.enqueue(node(155, 6))
pq.enqueue(node(855, 9))
pq.enqueue(node(877, 8))

pq.display()
