import heapq as h
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        origin = [0,0]

        for x, y in points:
            distance = math.sqrt((origin[0]-x)**2+(origin[1]-y)**2)
            item = (-distance, [x,y])
            h.heappush(heap, item)

            if len(heap) > k:
                h.heappop(heap)
        
        res = []
        for _, item in heap:
            res.append(item)
        
        return res
