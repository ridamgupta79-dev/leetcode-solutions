class Solution(object):
    def threeSum(self, nums):
        
        result = set() 
        n = len(nums)

        for first in range (0, n) :
            my_set = set()
            for second in range (first+1, n) :
                third = 0 - nums[first] - nums[second]
                if third in my_set :
                    part = [nums[first], nums[second], third]
                    part.sort()
                    result.add(tuple(part))
                my_set.add(nums[second])
                    

        return [list(x) for x in result]
