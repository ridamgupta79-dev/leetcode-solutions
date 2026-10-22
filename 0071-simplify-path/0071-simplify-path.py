class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        paths = path.split("/")  
        result = ""

        for i in paths :
            if i == "" :
                continue
            if i == "." :
                continue
            if i == ".." :
                if stack :
                    stack.pop()

            else :
                stack.append(i)  

        for i in stack :
            result = result + "/" + i

        if result == "" :
            return "/"

        return result  

                