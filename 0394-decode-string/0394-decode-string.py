class Solution:
    def decodeString(self, s: str) -> str:

        s1 = []
        s2 = []
        num = 0

        for ch in s :
            if ch.isdigit() :
                num = num * 10 + int(ch)
            elif ch == "[" :
                s1.append(num)
                s2.append("[")
                num = 0
            elif ch == "]" :
                a = ""
                while s2[-1] != "[" :
                    a = s2.pop() + a

                s2.pop()

                k = s1.pop()
                s2.append(a * k)
            else:
                s2.append(ch)

        return "".join(s2)            