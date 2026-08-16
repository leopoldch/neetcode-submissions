from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        dic = {"}":"{", ")":"(", "]":"["}

        for c in s:
            if c in dic:
                should = dic[c]
                if len(stack) == 0:
                    return False
                if should != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

        


