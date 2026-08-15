class Solution:
    def hammingWeight(self, n: int) -> int:

        result = 0

        for i in range (0,32) :
            if n & (1<<i) != 0 :
                result += 1

        return result