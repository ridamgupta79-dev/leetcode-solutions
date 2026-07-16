class Solution(object):

    def gcdSum(self, nums):

        def find_gcd(a, b) :
            while b != 0 :
                a,b = b, a%b
            return abs(a)
        
        len_nums = len(nums)
        large = 0
        l1 = []

        for i in range (0, len_nums) :
            if nums[i] > large :
                large = nums[i]
            l1.append(find_gcd(nums[i], large))
        
        l1.sort()

        left = 0
        right = len(l1) - 1
        gcd_sum = 0

        while left < right :
            gcd_sum += find_gcd(l1[left], l1[right])

            left += 1
            right -= 1

        return gcd_sum 

        
        