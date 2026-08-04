class Solution(object):
    def findMissingElements(self, nums):

        min = float("inf")
        max = 0
        d = {}
        result = []

        for i in range (0, len(nums)) :
            if nums[i] < min :
                min = nums[i]
            if nums[i] > max :
                max = nums[i]
            d[nums[i]] = 0

        for i in range (min, max) :
            if i not in d :
                result.append(i)
        
        return result
            


