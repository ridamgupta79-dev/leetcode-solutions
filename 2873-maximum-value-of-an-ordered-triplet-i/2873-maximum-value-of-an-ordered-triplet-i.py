class Solution(object):
    def maximumTripletValue(self, nums):

        n = len(nums)
        result = float("-inf")

        for i in range (0, n) :
            for j in range (i+1, n) :
                for k in range (j+1, n) :
                    a = (nums[i] - nums[j]) * nums[k]
                    result = max(result,a)

        if result <= 0 :
            return 0
        else :
            return result