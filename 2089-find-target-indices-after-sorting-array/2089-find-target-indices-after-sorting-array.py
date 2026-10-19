class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        c1 = 0
        c2 = 0

        for i in range (0, len(nums)) :
            if nums[i] < target :
                c1 += 1
            elif nums[i] == target :
                c2 += 1

        return list(range(c1, c1+c2))