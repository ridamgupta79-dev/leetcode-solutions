class Solution(object):
    def productExceptSelf(self, nums):

        a = nums[:]
        b = nums[:]

        for i in range (1, len(a)) :
            a[i] = a[i] * a[i-1]

        for j in range(len(b)-2, -1, -1) :
            b[j] = b[j] * b[j+1]

        for k in range(0, len(nums)) :
            if k == 0 :
                nums[0] = b[1]
            elif k ==len(nums) - 1 :
                nums[len(nums)-1] = a[len(nums)-2]
            else :
                nums[k] = a[k-1] * b[k+1]

        return nums