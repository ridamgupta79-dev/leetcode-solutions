class Solution(object):
    def findDuplicate(self, nums):

        n = len(nums)
        hash = set()

        for i in range (0, n) :
            if nums[i] in hash :
                return nums[i]
            else :
                hash.add(nums[i])