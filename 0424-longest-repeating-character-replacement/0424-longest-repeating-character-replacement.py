class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d = {}
        left = 0
        result = 0
        freq = 0

        for right in range(len(s)) :

            if s[right] not in d :
                d[s[right]] = 0

            d[s[right]] += 1

            freq = max(freq, d[s[right]])

            window = right-left+1

            if window - freq > k :
                d[s[left]] -= 1
                left += 1

            window = right - left + 1
            result = max(result, window)

        return result
