class Solution(object):
    def findDuplicate(self, nums):

        i = 0
        j = 0

        while True :
            i = nums[i]
            j = nums[nums[j]]
            
            if i == j :
                break
            
        i = 0

        while True :
            i = nums[i]
            j = nums[j]

            if i==j :
                return i

        return i
