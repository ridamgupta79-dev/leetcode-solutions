class Solution(object):
    def maxProduct(self, nums):

        first = 0
        second = 0

        for i in range (0, len(nums)) :
            if nums[i] > first :
                second = first
                first = nums[i]
            elif nums[i] > second :
                second = nums[i]
        
        return (first-1) * (second-1)

        

        
        
        