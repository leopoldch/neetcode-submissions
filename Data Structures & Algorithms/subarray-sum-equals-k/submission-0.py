from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        viewedSums = defaultdict(int)
        amountOfSubarraySums = 0
        currentSum = 0
        viewedSums[currentSum] = 1

        for num in nums:
            currentSum += num
            needed = currentSum-k

            if needed in viewedSums:
                amountOfSubarraySums += viewedSums[needed]
            
            viewedSums[currentSum] +=1
        
        return amountOfSubarraySums
