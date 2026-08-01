class Solution(object):
    def subarraySum(self, nums, k):

        n = len(nums)
        d = {}
        d[0] = 1
        pre_sum = 0
        count = 0

        for i in range (0, n) :
            pre_sum += nums[i]

            if (pre_sum - k) in d :
                count += d[pre_sum-k]

            if pre_sum not in d :
                d[pre_sum] = 1
            else :
                d[pre_sum] += 1

        return count  