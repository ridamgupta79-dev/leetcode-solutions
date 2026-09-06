class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def subsets(aset, index) :
            result.append(aset[:])

            for i in range (index, len(nums)) :

                if i > index and nums[i] == nums[i-1] :
                    continue

                aset.append(nums[i])
                a = i+1
                subsets(aset, a)
                a = a-1
                aset.pop()

        subsets([],0)

        return result


