class Solution(object):
    def maxSubArray(self, nums):
        
        n = len(nums)
        sum = float("-inf")
        total = 0

        for i in range(0, n) :
            total = total + nums[i]
            sum = max(total, sum)

            if total < 0 :
                total = 0

        return sum