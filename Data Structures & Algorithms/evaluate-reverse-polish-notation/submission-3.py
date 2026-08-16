from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = deque()
        operators = set(['*', '+', '-', '/'])

        for token in tokens:
            if token in operators:
                last = d.pop()
                first = d.pop()
                operation = str(first) + token + str(last)
                result = eval(operation)
                d.append(int(result))
            else:
                d.append(int(token))
        
        return d.pop()