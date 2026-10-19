class Solution:
    def calPoints(self, operations: list[str]) -> int:

        stack = []

        for i in operations :
            if i == "C" :
                stack.pop()
            elif i == "D" :
                stack.append(stack[-1]*2)
            elif i == "+" :
                stack.append(stack[-1]+stack[-2])
            else :
                stack.append(int(i))
        
        sum = 0

        for i in stack :
            sum += i
        
        return sum