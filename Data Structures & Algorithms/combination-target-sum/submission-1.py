class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, current, total):
            if total == target:
                res.append(list(current))
                return

            if i> len(nums)-1 or target< total:
                return

            val = nums[i]

            current.append(val)
            backtrack(i, current, total+val)
            current.pop()
            backtrack(i+1, current, total)

        backtrack(0,[],0)
        return res