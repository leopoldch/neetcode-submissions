from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        d = deque()

        for idx in range(len(temperatures)-1, -1, -1):

            while d and temperatures[d[-1]] <= temperatures[idx]:
                d.pop()
            
            if d:
                res[idx] = d[-1]-idx     

            d.append(idx)

        return res