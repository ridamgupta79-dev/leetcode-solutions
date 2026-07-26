class Solution(object):
    def validPalindrome(self, s):

        def Palindrome(i,j) :
            while i < j :
                if s[i] != s[j] :
                    return False
                i+=1
                j-=1
            return True

        i = 0
        j = len(s) - 1

        while i < j :
            if s[i] == s[j] :
                i+=1
                j-=1
            else :
                return (Palindrome(i+1, j) or (Palindrome(i, j-1)))
        return True



       

        
        