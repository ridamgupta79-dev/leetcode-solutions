class Solution(object):
    def twoSum(self, numbers, target):

        nums = numbers
        n = len(nums)
        i = 0
        j = n-1

        while i <= j :
            if nums[i] + nums[j] == target :
                return [i+1, j+1]
            elif nums[i] + nums[j] < target :
                i+=1
            else :
                j-=1

        

      

        

           

        


                
        
        