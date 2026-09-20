class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        position = 0

        for i in range(len(s)):
            reverse_pos = ord('z') - ord(s[i]) + 1
            position = i + 1

            result += reverse_pos * position

        return result
