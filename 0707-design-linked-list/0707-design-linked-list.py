class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        current = self.head
        for i in range(0, index):
            current = current.next
        return current.val
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        new_Node = Node(val)
        if index == 0:
            new_Node.next = self.head
            self.head = new_Node
        else:
            current = self.head
            for i in range(0, index - 1):
                current = current.next
            new_Node.next = current.next
            current.next = new_Node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        if index == 0:
            temp = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            for i in range(0, index - 1):
                current = current.next
            temp = current.next
            current.next = current.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)