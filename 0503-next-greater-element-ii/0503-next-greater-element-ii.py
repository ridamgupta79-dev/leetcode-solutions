class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        stack = []
        ans = [-1] * len(nums)

        for i in range (2 * len(nums)-1, -1, -1)  :
            while stack and nums[stack[-1]] <= nums[i%len(nums)] :
                stack.pop()

            if i < len(nums) and stack :
                if len(stack) != 0 :
                    ans[i] = nums[stack[-1]]

            stack.append(i%len(nums))

        return ans  