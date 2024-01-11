class node():
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next
        
class stack():
    def __init__(self, head=None, pointer=None) -> None:
        self.head = node(value=head, next=pointer)
        if self.head.value == None:
            self.size = 0
        else:
            self.size = 1
    def __str__(self) -> str:
        if self.size > 0:
            curr = self.head
            out = ''
            while curr != None:
                out += '->'+f'{curr.value}'
                curr = curr.next
            return out[2:]
    def getSize(self):
        return self.size
    def peek(self):
        if self.size == 0:
            raise Exception('Stack is empty')
        else:
            return self.head.value
    def push(self, value):
        if self.size == 0:
            self.head = node(value=value)
        else:
            new_node = node(value=value,next=self.head)
            self.head = new_node
        self.size += 1
    def remove(self):
        if self.size == 0:
            raise Exception('Stack is empty')
        else:
            temp = self.head.value
            self.head = self.head.next
            self.size -= 1
            return temp


mystack = stack()  
for i in range(1,10):
    mystack.push(i)