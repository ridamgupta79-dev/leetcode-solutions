"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None :
            return None

        l1 = []
        temp = head

        while temp :

            if temp.child :
                if temp.next :
                    l1.append(temp.next)

                temp.next = temp.child
                temp.next.prev = temp
                temp.child = None

            if temp.next is None :
                if l1 :
                    next = l1.pop()

                    temp.next = next
                    next.prev = temp

            temp = temp.next
        
        return head
            


