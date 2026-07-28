class Solution(object):
    def smallestPalindrome(self, s):

        d = {}

        for i in s :
            if i in d :
                d[i] += 1
            else :
                d[i] = 1

        ld = list(d)
        ld.sort()

        left = ""
        mid = ""
        right = ""

        for i in ld :
            total = d[i]
            half = total // 2

            for j in range(half) :
                left += i
            if total % 2== 1 :
                mid = i

        for i in range (len(left)-1, -1, -1) :
            right += left[i]

        answer = left + mid + right
        return answer        
        