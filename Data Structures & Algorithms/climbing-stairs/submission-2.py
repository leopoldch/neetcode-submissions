class Solution:

    def __init__(self):
        self.nb = 0

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        def fibo(prev, cur):
            value = prev+cur
            self.nb+=1
            if self.nb == n-1:
                return value

            return fibo(cur, value)
        
        return fibo(1,1)