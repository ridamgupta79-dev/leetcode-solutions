# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        tempa = headA
        tempb = headB
        counta = 0
        countb = 0
        
        while tempa :
            counta += 1
            tempa = tempa.next

        while tempb :
            countb += 1
            tempb = tempb.next

        tempa, tempb = headA, headB 

        if counta > countb :
            for _ in range(counta-countb) :
                tempa = tempa.next
        elif counta < countb :
            for _ in range (countb - counta) :
                tempb = tempb.next

        while tempa != tempb :
            tempa = tempa.next
            tempb = tempb.next

        return tempa



        