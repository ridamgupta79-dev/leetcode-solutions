class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        total = 0
        nums.sort()

        mid = nums[len(nums)//2]

        for i in nums :
            total += abs(i - mid)

        return total
    
