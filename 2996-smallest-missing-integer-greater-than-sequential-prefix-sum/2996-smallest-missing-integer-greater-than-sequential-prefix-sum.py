class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        i = 1
        sum = nums[0]
        hash_set = set()
        hash_set.add(nums[0])

        while i< len(nums) and nums[i] == nums[i-1] + 1 :
            sum += nums[i]
            i += 1

        for j in range (0, len(nums)) :
            hash_set.add(nums[j])

        while sum in hash_set :
            sum += 1
            
        return sum

