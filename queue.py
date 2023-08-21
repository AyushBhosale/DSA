class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class queue():
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
    def dequeue(self):
        if self.first is None:
            return None
        elif self.length==1:
            self.last=None
            self.first=None
        else:
            temp=self.first.next
            self.first.next=None
            self.first=None
            self.first=temp

q=queue(7)
q.enqueue(2)
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
q.dequeue()
q.print_queue()