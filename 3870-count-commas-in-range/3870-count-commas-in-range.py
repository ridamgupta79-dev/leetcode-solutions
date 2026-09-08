class Solution:
    def countCommas(self, n: int) -> int:

        result = 0

        if len(str(n)) < 4 :
            return 0

        for i in range (1000,n+1) :
            number = len(str(i))
            a = (number-1)//3
            result += a

        return result 
