class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        result = 0
        l = set()

        for right in range(len(s)) :

            while s[right] in l :
                l.remove(s[left])
                left += 1
            
            l.add(s[right])
            
            result = max(result, right-left+1)

        return result