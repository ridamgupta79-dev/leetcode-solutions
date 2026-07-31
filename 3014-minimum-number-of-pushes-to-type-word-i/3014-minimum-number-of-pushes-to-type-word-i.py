class Solution(object):
    def minimumPushes(self, word):

        n = len(word)

        if n <= 8 :
            return n
        elif n <= 16 :
            return 8 + ((n-8)*2)
        elif n <= 24 :
            return 24 + ((n-16)*3)
        else :
            return 48 + ((n-24)*4)
        
        