import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:return 0

        heap_stones = []

        for stone in stones: # O(n*log(n))
            heapq.heappush(heap_stones, -stone) 

        while len(heap_stones) > 1:

            first_big_stone = -heapq.heappop(heap_stones)
            second_big_stone = -heapq.heappop(heap_stones)

            if first_big_stone == second_big_stone:
                continue

            new_weight = first_big_stone-second_big_stone
            heapq.heappush(heap_stones, -new_weight) 
        

        if len(heap_stones) == 0:
            return 0


        return -heapq.heappop(heap_stones)


            

