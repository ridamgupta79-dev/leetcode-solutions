class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range (0, len(nums)) :
            a = nums[i]
            sum = 0

            while a > 0 :
                sum += a%10
                a = a // 10
            if sum == i :
                return sum

        return -1
            