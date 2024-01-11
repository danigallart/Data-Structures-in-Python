import numpy as np

class node():
    def __init__(self,value=None,next=None) -> None:
        self.value = value
        self.next = next

class linkedList():
    def __init__(self, head=None, pointer=None) -> None:
        self.head = node(value=head, next=pointer)
        if self.head.value == None:
            self.size = 0
        else:
            self.size = 1
    def __str__(self) -> str:
        if self.size == 0:
            raise Exception('Empty linked list')
        else:
            curr = self.head
            out = ''
            for _ in range(self.size):
                out += '->'+ f'{curr.value}'
                curr = curr.next                
            return out[2:]
    def insertAtBegin(self, value):
        if self.size > 0:
            old_node = self.head
            self.head = node(value,old_node)
            self.size += 1
        else:
            self.head = node(value,None)
            self.size += 1
    def getSize(self):
        return self.size
    def addAtIndex(self, value=None, index=None):
        new_node = node(value, next=None)
        if self.head > 0:
            if index == 0:
                self.insertAtBegin(value=value)
            elif self.size > index:
                temp = self.head
                for _ in range(index):
                    prev = temp
                    temp = temp.next
                new_node.next = temp
                prev.next = new_node
                self.size += 1
            elif self.size <= index:
                temp = self.head
                for _ in range(self.size - 1):
                    temp = temp.next
                temp.next = new_node
                self.size += 1
        else:
            self.insertAtBegin(value=value)
    def removeAtIndex(self, index):
        if self.size > 0:
            if index == 0:
                val = self.head.value
                self.head = self.head.next
                self.size -= 1
                return val
            elif index < self.size:
                curr = self.head
                for _ in range(index):
                    prev = curr
                    curr = curr.next
                prev.next = curr.next
                self.size -= 1
                return curr.value
            elif index == self.size:
                curr = self.head
                for _ in range(index-1):
                    curr = curr.next
                val = curr.value
                del curr
                self.size -= 1
                return val
            elif index > self.size:
                raise Exception('Index exceeds linked list size')
                

mylinkedlist = linkedList()
mylinkedlist.insertAtBegin(1)
mylinkedlist.insertAtBegin(2)
mylinkedlist.insertAtBegin(3)
mylinkedlist.insertAtBegin(4)

print(mylinkedlist)