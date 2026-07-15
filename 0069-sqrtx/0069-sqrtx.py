class Solution(object):
    def mySqrt(self, x):

        if x < 2 :
            return x

        l = 1
        r = x
        ans = 0

        while l <= r:

            mid = (l + r) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                ans = mid
                l = mid + 1

            else:
                r = mid - 1

        return ans
        
        