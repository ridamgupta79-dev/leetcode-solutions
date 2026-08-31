# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        if head is None or head.next is None or head.next.next is None :
            return [-1,-1]

        back = head
        temp = head.next
        front = temp.next

        l = []
        count = 1
        mindistance = float("inf")

        while front is not None :
            if ((temp.val > back.val and temp.val > front.val)or(temp.val<back.val and temp.val<front.val)) :
                
                if len(l) != 0 :
                    mindistance = min(mindistance, (count-l[-1]))
                l.append(count)

            count += 1

            back = temp
            temp = front
            front = temp.next

        if len(l) < 2 :
            return [-1,-1]
        return (mindistance, (l[-1]-l[0]))



        