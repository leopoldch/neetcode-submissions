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
        starts = [x.start for x in sorted(intervals, key=lambda x: x.start)]
        ends = [x.end for x in sorted(intervals, key=lambda x: x.end)]

        n = len(starts)
        start, end = 0, 0
        count = 0
        max_seen = 0

        while start < n:

            if starts[start] < ends[end]:
                count+=1
                start+=1
            else:
                count -= 1
                end += 1
            
            max_seen = max(max_seen, count)
            
        return max_seen
