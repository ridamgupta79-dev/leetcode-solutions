class Solution(object):
    def plusOne(self, digits):

        n = len(digits)
        d = 0
        l = []

        for i in range (n) :
            d = (d*10) + digits[i]

        d = d + 1

        dl = [int(digit) for digit in str(d)]

        return dl


        