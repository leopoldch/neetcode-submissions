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

        intervals = sorted(intervals, key=lambda x:(x.start, x.end))
        last = None
        for idx, interval in enumerate(intervals):
            if idx == 0:
                last = interval
                continue
            
            if interval.start < last.end:
                return False
            
            last = interval
        
        return True
            


