class Solution:

    def climbStairs(self, n: int) -> int:

        if n ==1:return 1

        def fibo(prev, cur, cur_n):
            value = prev+cur
            cur_n+=1
            if cur_n >= n:
                return value

            return fibo(cur, value, cur_n)
        
        return fibo(1,1, 1)