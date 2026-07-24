class Solution(object):
    def runningSum(self, nums):
        
        n = len(nums)
        
        for i in range (n-1, -1, -1) :
            if i == 0 :
                nums[i] = nums[i]
            
            else :
                sum = 0
                for j in range (i, -1, -1) :
                    sum += nums[j]

                nums[i] = sum

        return nums
       
        