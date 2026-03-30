class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(0,len(prices)-1):
            for j in range(i,len(prices)):

                if prices[i] < prices[j]:
                    profit = max(profit,prices[j]-prices[i])

        return profit