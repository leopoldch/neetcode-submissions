from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        result = []
        heapq.heapify(result)

        for val, occurences in counter.items():
            
            item = (occurences, val)

            heapq.heappush(result,item)

            if len(result) >k:
                heapq.heappop(result)
        
        return [val for _,val in result]



            