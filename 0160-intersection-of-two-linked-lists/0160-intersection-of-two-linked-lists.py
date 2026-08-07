# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        tempa = headA
        tempb = headB
        mset = set()

        while tempa :
            mset.add(tempa)
            tempa = tempa.next

        while tempb :
            if tempb in mset :
                return tempb
            else :
                tempb = tempb.next

        return None

        