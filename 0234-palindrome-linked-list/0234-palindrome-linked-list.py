# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head.next :
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        back = None

        while second :
            front = second.next
            second.next = back
            back = second
            second = front

        first = head
        second = back

        while second :
            if first.val != second.val :
                return False

            first = first.next
            second = second.next

        return True
