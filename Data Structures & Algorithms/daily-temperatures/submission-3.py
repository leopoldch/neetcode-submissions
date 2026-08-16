from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = deque()

        for index in range(n-1,-1,-1):
            current_temp = temperatures[index]
            while stack and current_temp >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                result[index] = stack[-1] - index
             
            stack.append(index)

        return result
        