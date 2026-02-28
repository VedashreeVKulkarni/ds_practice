class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                profit = max(profit, price - buy)
        return profit
