class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        result = len(nums)

        for i in range (0, len(nums)) :
            result ^= i
            result ^= nums[i]

        return result