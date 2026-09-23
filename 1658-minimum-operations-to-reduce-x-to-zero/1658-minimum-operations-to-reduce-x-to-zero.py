class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        total = 0
        for i in range (0, len(nums)) :
            total += nums[i]

        target = total - x

        if target < 0 :
            return -1
        if target == 0 :
            return len(nums)

        left = 0
        right = 0
        tsum = 0
        tlen = -1

        while right < len(nums) :
            tsum += nums[right]

            while tsum > target :
                tsum -= nums[left]
                left += 1

            if tsum == target :
                tlen = max(tlen, right-left+1)

            right += 1

        if tlen == -1 :
            return -1
        else :
            return len(nums) - tlen

        
               