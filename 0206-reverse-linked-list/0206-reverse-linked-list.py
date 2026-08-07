# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        temp = head
        back = None

        while temp is not None :
            front = temp.next
            temp.next = back
            back = temp
            temp = front
        
        return back