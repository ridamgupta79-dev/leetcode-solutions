class Solution(object):
    def pivotIndex(self, nums):

        n = len(nums)

        lsum = [0] * n
        rsum = [0] * n

        for i in range(1, n):
            lsum[i] = lsum[i - 1] + nums[i - 1]

        for i in range(n - 2, -1, -1):
            rsum[i] = rsum[i + 1] + nums[i + 1]

        for i in range(0, n):
            if lsum[i] == rsum[i]:
                return i
    
        return -1

        



        
        