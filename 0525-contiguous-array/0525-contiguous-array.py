class Solution(object):
    def findMaxLength(self, nums):

        d = {}
        d[0] = -1
        count = 0
        n = len(nums)
        ans = 0

        for i in range (n) :
            if nums[i] == 0 :
                nums[i] = -1

        for i in range (n) :
            count += nums[i]

            if count not in d:
                d[count] = i
            else :
                ans = max(ans, (i - d[count]))
        
        return ans
