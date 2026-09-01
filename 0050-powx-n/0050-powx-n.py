class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0 :
            x = 1/x
            n = -n

        def pow(num) :
            if num == 0 :
                return 1

            half = pow(num//2)

            if num % 2 == 0 :
                return half * half
            else :
                return half * half * x

        return pow(n)
