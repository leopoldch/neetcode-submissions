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
                print(operation)
                result = eval(operation)
                print(result)
                d.append(int(result))
            else:
                d.append(int(token))
        
        print(d)
        result = d.pop()

        return result