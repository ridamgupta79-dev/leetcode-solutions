class Solution(object):
    def sortColors(self, nums):

        c1 = 0
        c2 = 0
        c0 = 0
        n = len(nums)

        for i in range (0, n) :
            if nums[i] == 0 :
                c0 +=1
            elif nums[i] == 1 :
                c1 += 1
            elif nums[i] == 2 :
                c2 += 1

        nums[0:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:n] = [2] * c2

        return nums


     
            
           
        
       
        
        