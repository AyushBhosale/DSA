class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp=self.head
        while self.head is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.head
            self.head.prev=new_node
            self.head=new_node
            self.head.next=temp
            self.head.prev=None
        return True
    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        if self.head ==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        if index>=self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp=self.tail
            for _ in range(index,self.length-1):
                temp=temp.prev
        return temp.value

    def set_value(self, index, value):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value=value
    # def insert(self,index,value):
    #     if index<0 or index>self.length:
    #         return None
    #     if index==0:
    #         return self.prepend()
    #     if index==self.length:
    #         return self.append()
    #     new_node=Node(value)
    #     temp=self.head
    #     for _ in range(index):
    #         temp=temp.next
    #     new_node.prev = temp.prev
    #     temp.prev=new_node
    #     new_node.next=temp
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
           return self.popfirst()
        if index==self.length-1:
            return self.pop()
        tem






my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.set_value(3,5)
my_doubly_linked_list.set_value(2,8)

my_doubly_linked_list.print_list()
 
