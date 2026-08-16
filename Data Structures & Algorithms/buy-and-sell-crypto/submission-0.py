class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen = 1000000
        max_profit = 0

        for index in range(len(prices)):
            current = prices[index]

            if current - lowest_seen > max_profit:
                max_profit = current - lowest_seen

            if lowest_seen > current:
                lowest_seen = current
        
        return max_profit
        