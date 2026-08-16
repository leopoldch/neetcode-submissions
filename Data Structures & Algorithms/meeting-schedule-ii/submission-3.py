"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        res= []
        max_seen = float("-inf")
        for interval in intervals:

            start = interval.start
            end = interval.end
            item = (end, start)
            heapq.heappush(res, item)
            max_seen = max(end, max_seen)

        occupancy = [0]*max_seen

        while res:
            end, start = heapq.heappop(res)
            for i in range(start, end):
                occupancy[i]+=1

        return max(occupancy)

        









