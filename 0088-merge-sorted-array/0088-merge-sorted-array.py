class Solution(object):
    def merge(self, nums1, m, nums2, n):

        m = len(nums2)
        last = -1

        for i in range (0, m) :
            nums1[last] = nums2[i]
            last -= 1

        nums1.sort()
        print(nums1)
        
        