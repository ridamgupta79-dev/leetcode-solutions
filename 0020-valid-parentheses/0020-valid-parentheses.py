class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for b in s :
            if b == '{' or b == '(' or b == '[' :
                stack.append(b) 
            else :
                if len(stack) == 0 :
                    return False
                ch = stack.pop()
                if (
                    (b == ')' and ch == '(') or
                    (b == ']' and ch == '[') or 
                    (b == '}' and ch == '{')
                ) :
                    continue

                else :
                    return False

        return len(stack) == 0