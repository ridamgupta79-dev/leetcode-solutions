class Solution(object):
    def maxProduct(self, n):

        large = float("-inf")
        second_large = float("-inf")

        while n > 0 :
            ld = n % 10

            if ld > large :
                second_large = large
                large = ld
            elif ld > second_large :
                second_large = ld

            n = n // 10

        return large * second_large        
        