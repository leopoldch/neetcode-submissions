"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals = sorted(intervals, key=lambda interval: (interval.start, interval.end))
        last = None
        for interval in intervals:
            if last is None:
                last = interval
                continue
            
            if interval.start < last.end:
                return False
            
            last = interval
        
        return True


