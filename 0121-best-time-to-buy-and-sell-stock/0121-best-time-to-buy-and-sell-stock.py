class Solution(object):
    def maxProfit(self, prices):
        
        n = len(prices)
        i = 0
        j = 1
        profit = 0

        while j < n :
            if prices[i] > prices[j] :
                i = j
                j += 1
            else :
                pro = prices[j] - prices[i]
                profit = max(profit, pro)
                j += 1
        
        return profit
        