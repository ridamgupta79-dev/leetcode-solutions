class Solution(object):
    def removeElement(self, nums, val):

        n = len(nums)
        j = 0

        for i in range (0, n) :
            if nums [i] != val :
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return j
       
        