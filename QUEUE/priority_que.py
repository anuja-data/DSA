class node:
    def __int__(self,value,pr):
        self.data=value
        self.priority=pr
        self.next=None
class PriorityQueue:
    def __int__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.front.priority>new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return
        else:
            temp=self.front
            while temp.next:
                if new_node.priority <= temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next
            prev.next=new_node
            new_node.next=temp

    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    #create priority Queue
pq=PriorityQueue()
pq.enqueue(node(100,56))
pq.enqueue(node(155,67))
pq.enqueue(node(855,998))
pq.enqueue(node(877,56))



                   

        
