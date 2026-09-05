class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        cur = prices[0]

        for n in prices:
            gain = n-cur
            total_profit = max(total_profit,gain)
            if n < cur:
                cur = n
            
        return total_profit