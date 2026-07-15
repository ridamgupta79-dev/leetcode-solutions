class Solution(object):
    def gcdOfOddEvenSums(self, n):
        
        odd_sum = 0
        even_sum = 0
        gcd = 1

        for i in range (1, n*2, 2) :
            odd_sum += i

        for i in range (2, n*2 + 1, 2) :
            even_sum += i

        while even_sum > 0 :
            gcd = odd_sum % even_sum
            odd_sum = even_sum
            even_sum = gcd

       
        return odd_sum

        
        
        