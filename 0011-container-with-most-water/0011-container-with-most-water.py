class Solution(object):
    def maxArea(self, height):

        n = len(height)
        maxi = 0

        left = 0
        right = n-1

        while left < right :
            if height[left] < height[right] :
                area = (right-left) * height[left]
                maxi = max(area, maxi)
                left += 1

            else :
                area = (right - left) * height[right]
                maxi = max(area, maxi)
                right -= 1

        return maxi

            
            

        



        
        
        