class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        hash1 = {}
        result = 0

        for i in range (0, len(nums1)) :
            for j in range (0, len(nums2)) :
                sum = nums1[i] + nums2[j]

                if sum not in hash1 :
                    hash1[sum] = 1
                else :
                    hash1[sum] += 1

        for i in range (0, len(nums3)) :
            for j in range (0, len(nums4)) :

                needed = 0 - (nums3[i]+nums4[j])

                if needed in hash1 :
                    result += hash1[needed]

        return result