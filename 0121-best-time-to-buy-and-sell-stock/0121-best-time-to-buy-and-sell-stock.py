class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        buy=prices[0]
        profit=0

        for i in range(1,len(prices)):
           if prices[i]<buy:
            buy=prices[i]
           else:
            sell=prices[i]
            curr_profit=sell-buy
            if curr_profit>profit:
                profit=curr_profit

        return profit        

   