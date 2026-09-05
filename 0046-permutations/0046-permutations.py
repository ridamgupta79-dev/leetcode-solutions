class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        aset = set()

        def perm(l) :

            if len(l) == len(nums) :
                result.append(l[:])
                return

            for i in range (len(nums)) :

                if nums[i] in aset :
                    continue

                l.append(nums[i])
                aset.add(nums[i])

                perm(l)

                l.pop()
                aset.remove(nums[i])

        perm([])

        return result

