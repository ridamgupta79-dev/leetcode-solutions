class Solution(object):
    def reverse(self, x):

            num = x
            n = abs(num)
            result = 0

            while n > 0 :
                ld = n % 10
                result = (result * 10) + ld
                n = n // 10

            if -2**31 < result < 2**31 - 1 :

                if num > 0 :
                    return result
                elif num < 0 :
                    return 0-result
                else :
                    return 0
                
            else : 
                return 0

        
            
            


        
        