class Solution(object):
    def majorityElement(self, nums):
        
        n = len(nums)
        d = {}

        for i in range (0, n) :
            if nums[i] in d :
                d[nums[i]] += 1
            else :
                d[nums[i]] = 0
        
        return max(d, key=d.get)

        