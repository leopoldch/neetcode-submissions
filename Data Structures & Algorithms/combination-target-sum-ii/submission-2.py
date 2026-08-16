class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(idx, currentArray, total):
            if total == target:
                result.append(list(currentArray))
                return
            
            if idx > len(candidates)-1 or total > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                val = candidates[i]
                currentArray.append(val)
                backtrack(i + 1, currentArray, total + val)
                currentArray.pop()
            
        backtrack(0,[],0)

        return result
