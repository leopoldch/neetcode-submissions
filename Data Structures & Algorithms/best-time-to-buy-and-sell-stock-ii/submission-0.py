class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lastBought = prices[0]
        total = 0

        for i in range(1,len(prices)):
            currentElement = prices[i]
            # 2 choices 
            profit = currentElement-lastBought
            if profit > 0:
                total += profit

            lastBought = currentElement
        
        return total

