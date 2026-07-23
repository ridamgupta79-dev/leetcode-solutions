class Solution(object):
    def removeDuplicates(self, nums):

        n = len(nums)
        i = 0

        for j in range (0, n) :
            if nums[j] != nums[i] :
                i+=1
                nums[i], nums[j] = nums[j], nums[i]

        return i + 1
        


       
        