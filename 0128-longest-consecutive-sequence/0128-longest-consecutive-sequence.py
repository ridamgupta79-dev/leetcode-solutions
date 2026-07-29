class Solution(object):
    def longestConsecutive(self, nums):

        if len(nums) == 0 :
            return 0 
        
        hash_set = set(nums)

        result = 0

        for i in hash_set :

            if (i-1) not in hash_set :
                length = 1
                current = i

                while (current+1) in hash_set :
                    current += 1
                    length += 1

                result = max(result, length)

        return result