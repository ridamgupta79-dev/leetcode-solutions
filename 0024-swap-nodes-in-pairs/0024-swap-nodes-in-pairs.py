# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        back = dummy

        while back.next and back.next.next :
            first = back.next
            second = first.next

            first.next = second.next
            second.next = first
            back.next = second

            back = first

        return dummy.next


