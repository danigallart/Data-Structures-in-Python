import numpy as np

class node():
    def __init__(self,value=None,next=None) -> None:
        self.value = value
        self.next = next

class linkedList():
    def __init__(self, head=None, pointer=None) -> None:
        self.head = node(value=head, next=pointer)
    def insertAtBegin(self, value):
        if self.head != None:
            old_node = self.head
            self.head = node(value,old_node)
        else:
            self.head = node(value,None)
    def length(self):
        if self.head == None:
            return 0
        else:
            counter = 0
            temp = self.head
            while temp != None:
                temp = temp.next
                counter += 1
            return counter
    def addAtIndex(self, value=None, index=None):
        new_node = node(value, next=None)
        if self.head != None:
            if self.length() > index:
                temp = self.head
                for _ in range(index):
                    prev = temp
                    temp = temp.next
                new_node.next = temp
                prev.next = new_node
            if self.length() <= index:
                temp = self.head
                for _ in range(self.length()-1):
                    temp = temp.next
                temp.next = new_node

