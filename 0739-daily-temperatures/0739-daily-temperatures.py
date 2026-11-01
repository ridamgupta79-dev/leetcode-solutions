class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1) :
            while stack and temperatures[stack[-1]] <= temperatures[i] :
                stack.pop()
            if stack :
                ans[i] = stack[-1] - i
            stack.append(i)
    
        
        return ans

