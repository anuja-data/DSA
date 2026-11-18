class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        temp=self.front
        print("deleted node:",temp.data)
        self.front=self.front.next
        if self.front==None:
            self.rear=None
        temp=None
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
que=LQueue()
que.enqueue(Node(23))
que.enqueue(Node(75))
que.enqueue(Node(28))
que.enqueue(Node(93))
que.print()
