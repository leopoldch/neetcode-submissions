class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:
            last_idx = len(stack)-1

            if op == "+":
                first_prev = int(stack[last_idx])
                second_prev = int(stack[last_idx-1])
                stack.append(first_prev+second_prev)
                continue
            
            if op == "C":
                stack.pop()
                continue
            
            if op == "D":
                last_doubled = int(stack[last_idx])*2
                stack.append(last_doubled)
                continue
            
            stack.append(int(op))
        
        return sum(stack)
