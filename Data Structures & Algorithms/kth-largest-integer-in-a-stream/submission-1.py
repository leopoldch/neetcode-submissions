import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numbers = []
        heapq.heapify(self.numbers)
        self.k = k 

        for num in nums:
            heapq.heappush(self.numbers, num)
            if len(self.numbers) > k:
                heapq.heappop(self.numbers)
            
    def add(self, val: int) -> int:
        heapq.heappush(self.numbers, val)
        if len(self.numbers) > self.k:
                v = heapq.heappop(self.numbers)
        
        return self.numbers[0]
