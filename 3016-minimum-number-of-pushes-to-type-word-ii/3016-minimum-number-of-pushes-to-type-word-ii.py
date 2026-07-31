class Solution(object):
    def minimumPushes(self, word):

        s = word
        hash_set = {}

        for i in s :
            if i not in hash_set :
                hash_set[i] = 1
            else :
                hash_set[i] += 1
        
        value = list(hash_set.values())
        value.sort(reverse=True)

        n = len(value)
        result = 0

        for i in range (0, n) :
            if i < 8 :
                result += value[i]*1
            elif i < 16 :
                result += value[i]*2
            elif i < 24 :
                result += value[i]*3
            else :
                result += value[i]*4
        
        return result
        


        