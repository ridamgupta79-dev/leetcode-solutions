# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right :
            return head

        dummy = ListNode(0)
        dummy.next = head

        back = dummy

        for _ in range (left-1) :
            back = back.next
        
        current = back.next

        for _ in range (right-left) :
            front = current.next
            current.next = front.next
            front.next = back.next
            back.next = front
        
        return dummy.next

        
        
