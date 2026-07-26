class Solution(object):
    def isPalindrome(self, s):

        sort_string = []

        for ch in s :
            if ch.isalnum() :
                sort_string.append(ch.lower())

        i = 0
        j = len(sort_string) - 1

        while i < j :
            if sort_string[i] != sort_string[j] :
                return False
            
            i += 1
            j -= 1

        return True


        

        