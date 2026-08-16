from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = defaultdict(int)
        majorityElementArray = []

        for num in nums:
            counter[num]+=1
        
        for number, occurences in counter.items():
            if occurences > n/3:
                majorityElementArray.append(number)
        
        return majorityElementArray
