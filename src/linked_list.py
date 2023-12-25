import numpy as np

class node():
    def __init__(self,value=None,next=None) -> None:
        self.value = value
        self.next = next

class linkedList():
    def __init__(self, head=None, pointer=None) -> None:
        self.head = node(value=head, next=pointer)

