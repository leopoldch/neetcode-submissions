class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):

            for coin in coins:
                rest = i - coin
                
                if rest == 0:
                    dp[i] = 1
                    break

                if rest < 0:
                    continue
                
                if dp[rest] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[rest]+1
                    else:
                        dp[i] = min(dp[i], dp[rest]+1)
        
        return dp[amount]

        