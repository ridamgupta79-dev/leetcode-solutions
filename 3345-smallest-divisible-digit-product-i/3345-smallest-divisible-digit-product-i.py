class Solution(object):
    def smallestNumber(self, n, t):

        while True :
            pro = 1
            for c in str(n) :
                pro *= int(c)
            if pro % t == 0 :
                return n
            n += 1  