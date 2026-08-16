class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:

            if op == "+":
                first_prev = int(stack[-1])
                second_prev = int(stack[-2])
                stack.append(first_prev+second_prev)
                continue
            
            if op == "C":
                stack.pop()
                continue
            
            if op == "D":
                last_doubled = int(stack[-1])*2
                stack.append(last_doubled)
                continue
            
            stack.append(int(op))
        
        return sum(stack)
