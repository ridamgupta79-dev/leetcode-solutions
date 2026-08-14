class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        d = {}
        left = 0
        result = 0

        for right in range (0, len(s)) :

            if s[right] not in d :
                d[s[right]] = 0
            d[s[right]] += 1
            
            while d[s[right]] > 2 :
                d[s[left]] -= 1
                left += 1

            result = max(result, right-left+1)

        return result

