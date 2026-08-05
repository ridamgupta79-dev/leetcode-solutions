class Solution(object):
    def maximumTripletValue(self, nums):

        n = len(nums)

        prefix = [0]*n
        prefix[0] = nums[0]

        suffix = [0]*n
        suffix[-1] = nums[-1]

        result = 0

        for i in range (1, n) :
            prefix[i] = max(prefix[i-1], nums[i])

        for i in range (n-2, -1, -1) :
            suffix[i] = max(suffix[i+1], nums[i])

        for i in range (1, n-1) :
            a = (prefix[i-1] - nums[i]) * suffix[i+1]
            result = max(result, a)

        return result

        
