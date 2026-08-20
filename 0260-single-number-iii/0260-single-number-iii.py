class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        start = 0

        for num in nums :
            start ^= num

        exclusive = 0

        while True :
            if (start & 1) == 1 :
                break 
            start >>= 1
            exclusive += 1

        one = 0
        two = 0

        for num in nums :
            if ((num >> exclusive) & 1) == 1 :
                one ^= num
            else :
                two ^= num

        return [one, two]     