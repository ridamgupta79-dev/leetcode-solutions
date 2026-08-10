class Node:
    def __init__(self, val) :
        self.val = val
        self.next  = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        if index < 0 :
            return -1
        temp = self.head
        for _ in range (index) :
            temp = temp.next
        if temp is None :
            return -1
        else :
            return temp.val
        
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        
    def addAtTail(self, val: int) -> None:
        new = Node(val)
        new.next = None
        if not self.head :
            self.head = new
        else :
            temp = self.head
            while temp and temp.next :
                temp = temp.next
            temp.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        temp = self.head
        if index < 0 :
            return 
        if index == 0 :
            self.addAtHead(val)
            return
        for _ in range (index-1) :
            if temp is None :
                return
            temp = temp.next
        if temp is None :
            return 
        new.next = temp.next
        temp.next = new
        

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if index < 0 :
            return 
        if index == 0 :
            self.head = temp.next
            return
        for _ in range (index-1) :
            if temp is None :
                return
            temp = temp.next
        if temp is None or temp.next is None :
            return
        temp.next = temp.next.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)