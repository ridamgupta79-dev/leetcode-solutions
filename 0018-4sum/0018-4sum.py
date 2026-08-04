class Solution(object):
    def fourSum(self, nums, target):

        n = len(nums)
        my_set = set()
        result = []

        for i in range (0, n) :
            for j in range (i+1, n) :
                hash_set = set()
                for k in range (j+1, n) :
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hash_set :
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        my_set.add(tuple(temp))
                    hash_set.add(nums[k])

        for ans in my_set :
            result.append(list(ans))
        
        return result