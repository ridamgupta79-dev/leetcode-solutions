class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def subsets(aset, start) :

            result.append(aset[:])

            for i in range(start, len(nums)) :

                aset.append(nums[i])
                a = i+1

                subsets(aset, a)

                a = a-1
                aset.pop()

        subsets([],0)

        return result

