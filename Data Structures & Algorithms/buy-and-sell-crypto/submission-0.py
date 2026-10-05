class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy=prices[0]
        best_profit=0
        for i in range(1, len(prices)):
            if prices[i]>lowest_buy:
                profit=prices[i]-lowest_buy
                if profit>best_profit:
                    best_profit=profit
            else:
                lowest_buy=prices[i]
        return best_profit