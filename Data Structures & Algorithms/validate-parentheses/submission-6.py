from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        d = deque()
        trad = {'(':')', '[': ']', '{':'}'}

        for car in s:
            if car in trad:
                d.append(car)
                continue
            
            if len(d) == 0:
                return False

            expected = trad[d.pop()]
            if expected != car:
                return False
        
        if len(d) > 0:
            return False

        return True
