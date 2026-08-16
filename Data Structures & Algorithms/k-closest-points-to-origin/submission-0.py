import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        closest_points = []
        heapq.heapify(closest_points)

        for x1, x2 in points:

            distance_to_origin = math.sqrt(x1**2+x2**2) # origin is set to 0,0

            item = (-distance_to_origin, [x1,x2])

            heapq.heappush(closest_points, item)

            if len(closest_points) > k:
                heapq.heappop(closest_points)

        results = []
        
        for _ in range(k):
            results.append(heapq.heappop(closest_points)[1])

        return results
