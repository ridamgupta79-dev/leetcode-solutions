class Solution(object):
    def threeSumClosest(self, nums, target):

        nums.sort()
        n = len(nums)
        close = float("inf")

        for i in range (0,n) :
            left = i+1
            right = n-1

            while left < right :

                sum = nums[i] + nums[left] + nums[right]

                if abs(target-sum) < abs(target-close) :
                    close = sum

                if sum < target :
                    left += 1

                elif sum > target :
                    right -= 1

                else :
                    return sum
        
        return close
