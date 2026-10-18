class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        n = len(asteroids)
        stack = []

        for i in range (0, n) :
            if asteroids[i] > 0 :
                stack.append(asteroids[i])

            else :
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()

                if stack and stack[-1] == abs(asteroids[i]) :
                    stack.pop()
                
                elif len(stack) == 0 or stack[-1] < 0 :
                    stack.append(asteroids[i])

        return stack

