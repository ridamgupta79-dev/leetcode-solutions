class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        total_subsets = 1<<n
        result = []

        for num in range (0, total_subsets) :
            sset = []
            for i in range (0, n) :
                if num & (1<<i) != 0 :
                    sset.append(nums[i])
            
            result.append(sset)

        return result