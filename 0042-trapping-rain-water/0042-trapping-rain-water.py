class Solution(object):
    def trap(self, height):

        n = len(height)
        left_high = []
        right_high = []

        for i in range (0, n) :
            if i == 0 :
                left_high.append(0)
            else :
                left_high.append(max(left_high[i-1], height[i-1]))
            
        
        for i in range (n-1, -1, -1) :
            if i == n-1 :
                right_high.append(0)
            else :
                j=0
                right_high.insert(0, max(right_high[j], height[i+1]))
                j += 1

        result = 0

        for i in range (0, n) :
            h = min(left_high[i], right_high[i]) - height[i]
            if h > 0 :
                result += h
        
        return result

