from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n

        d = deque()

        for i in range(n-1, -1, -1):
            current_temperature = temperatures[i]
            
            while d and temperatures[d[-1]] <= current_temperature:
                d.pop()
            
            if d:
                res[i] = d[-1] - i

            d.append(i)
        
        return res

        