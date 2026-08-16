class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        numsLength = len(nums)

        def backtrack(current, visitedSet):

            if len(current) == numsLength:
                results.append(list(current))
            
            for i in range(numsLength):
                if i not in visitedSet:
                    visitedSet.add(i)
                    current.append(nums[i])
                    backtrack(current, visitedSet)
                    current.pop()
                    visitedSet.remove(i)
            
            
        backtrack([], set())

        return results