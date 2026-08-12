class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        d = {}
        left = 0
        result = 0
        n = len(nums)

        for right in range (n) :

            if nums[right] not in d :
                d[nums[right]] = 0

            d[nums[right]] += 1
            
            while d[nums[right]] > k :
                d[nums[left]] -= 1
                left += 1

            result = max(result, right-left+1)
        
        return result