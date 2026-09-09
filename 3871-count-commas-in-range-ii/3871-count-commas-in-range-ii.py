class Solution:
    def countCommas(self, n: int) -> int:

        result = 0
        start = 1000

        while start <= n :

            result += n - start + 1
            start *= 1000

        return result