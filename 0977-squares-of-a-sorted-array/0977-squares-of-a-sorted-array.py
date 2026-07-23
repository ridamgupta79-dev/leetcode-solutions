class Solution(object):
    def sortedSquares(self, nums):

        n = len(nums)
        result = []

        for i in range (0, n) :
            result.append(abs(nums[i]) * abs(nums[i]))

        result.sort()
        return result


        
        
        