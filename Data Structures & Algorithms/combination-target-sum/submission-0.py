class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current, total):
            if total == target:
                res.append(list(current))
                return

            if i >= len(nums) or total > target:
                return

            value = nums[i]
            current.append(value)
            backtrack(i, current, total+value)

            current.pop()
            backtrack(i+1, current, total)
  
        backtrack(0, [], 0)
        return res   
                