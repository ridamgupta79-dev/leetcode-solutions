class Solution(object):
    def romanToInt(self, s):

        d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }

        result = 0 

        for i in range (0, len(s)) :
            present = d[s[i]]

            if i+1 < len(s) :
                next = d[s[i+1]]
            else :
                next = 0


            if present < next :
                result -= present
            else :
                result += present

        return result
        
        
        