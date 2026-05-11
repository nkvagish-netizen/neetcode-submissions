class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxProfit=0
        for i in range(len(prices)):
            sell=prices[i]
            profit=sell-buy
            if profit>maxProfit:
                maxProfit=profit
            if prices[i]<buy:
                buy=prices[i]
        return maxProfit
        