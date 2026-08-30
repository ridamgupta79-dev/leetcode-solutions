class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        maxindice = 0
        minindice = 0
        maxi = float("-inf")
        mini = float("inf")

        for i in range (0, len(nums)) :
            if nums[i] > maxi :
                maxi = nums[i]
                maxindice = i
            if nums[i] < mini :
                mini = nums[i]
                minindice = i

        fromfront = max(maxindice, minindice) + 1
        fromback = len(nums) - min(maxindice, minindice)
        mixed = (min(maxindice, minindice)+1) + (len(nums)-max(maxindice, minindice))

        return min(fromfront, fromback, mixed)
