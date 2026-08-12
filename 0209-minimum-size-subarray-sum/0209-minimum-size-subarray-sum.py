class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        result = float("inf")
        n = len(nums)
        sum = nums[0]

        if nums[0] >= target or nums[-1] >= target :
            return 1

        for right in range (1, n) :
            if left == right :
                break
            
            sum += nums[right]

            if sum >= target :
                result = min(result, right-left+1)
                while sum >= target :
                    result = min(result, right-left+1)
                    sum -= nums[left]
                    left += 1

        if result == float("inf") :
            return 0
        
        return result

            

