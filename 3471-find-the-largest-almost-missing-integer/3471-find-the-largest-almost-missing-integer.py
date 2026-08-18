class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        d = {}
        left = 0
        right = k-1

        while right < len(nums) :

            s = set()

            for i in range (left, right +1) :
                s.add(nums[i])
            for i in s :
                d[i] = d.get(i, 0) + 1

            left += 1
            right += 1

        result = -1

        for i in d :
            if d[i] == 1 :
                result = max(result, i)

        return result

