class Solution:
    def maxDepth(self, s: str) -> int:

        nd = 0
        temp = 0

        for i in range (0, len(s)) :
            if s[i] == "(" :
                temp += 1
                nd = max(nd, temp)

            elif s[i] == ")" :
                temp -= 1

        return nd
