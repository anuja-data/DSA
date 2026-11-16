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
                    temp=temp.next
                    
        
