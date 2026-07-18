def f(a, b) :
    while b > 0 :
        a, b = b, a%b
    return a






class Solution(object):
    def findGCD(self, nums):
        nums.sort()

        return f(nums[0], nums[-1])
        
        