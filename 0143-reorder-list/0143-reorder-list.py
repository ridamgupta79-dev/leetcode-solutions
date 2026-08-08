# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next :
            return None

        a = head
        b = head

        while b.next and b.next.next :
            a = a.next
            b = b.next.next

        back = None
        second = a.next
        a.next = None
        
        while second :
            front = second.next
            second.next = back
            back = second
            second = front

        first = head
        second = back

        while second :
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        return head


        