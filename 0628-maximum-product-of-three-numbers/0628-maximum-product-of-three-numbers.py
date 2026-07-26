class Solution(object):
    def maximumProduct(self, nums):

        nums.sort()

        if nums[-1] > 0:
            if nums[0] * nums[1] > nums[-2] * nums[-3] :
                return nums[-1] * nums[0] * nums[1]
            else :
                return nums[-1] * nums[-2] * nums[-3]
        else :
            return nums[-1] * nums[-2] * nums[-3]
       
        

       
        