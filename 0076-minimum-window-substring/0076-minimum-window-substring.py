class Solution:
    def minWindow(self, s: str, t: str) -> str:

        d1 = {}

        for letter in t :
            if letter not in d1 :
                d1[letter] = 0
            d1[letter] += 1

        left = 0
        d2 = {}
        count = 0
        result = float("inf")
        start = 0

        for right in range (0, len(s)) :
            if s[right] not in d2 :
                d2[s[right]] = 0
            d2[s[right]] += 1

            if s[right] in d1 and d2[s[right]] <= d1[s[right]] :
                count += 1

            while count == len(t) :
                if right-left+1 < result :
                    result = right-left+1
                    start = left
            
                d2[s[left]] -= 1

                if s[left] in d1 and d2[s[left]] < d1[s[left]] :
                    count -= 1
                
                left += 1

        if result == float("inf") :
            return ""

        return s[start:start+result]


