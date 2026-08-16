class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, current):
            
            if i > len(nums)-1:
                res.append(list(current))
                return
            res.append(list(current))

            for j in range(i, len(nums)):
                val = nums[j]

                current.append(val)

                backtrack(j+1,current)
                current.pop()


        backtrack(0,[])
        
        return res