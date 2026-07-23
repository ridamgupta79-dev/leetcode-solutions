class Solution(object):
    def sortColors(self, nums):

        n = len(nums)

        for i in range (0, n) :

            for j in range (i+1, n) :

                if nums[j] < nums[i] :
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
            
           
        
       
        
        