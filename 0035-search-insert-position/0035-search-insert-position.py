class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0
        highest = len(nums) - 1

        while low <= highest :
            middle = (highest+low)//2

            if nums[middle] == target :
                return middle
            elif nums[middle] < target :
                low = middle + 1
            else :
                highest = middle - 1

        return low 