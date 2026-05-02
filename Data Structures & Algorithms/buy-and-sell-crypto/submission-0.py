class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]

        for i in range(1,len(prices)):
            profit = prices[i]-lowest
            if profit<0:
                lowest = prices[i]
            maxProfit = max(profit,maxProfit)
        return maxProfit
        