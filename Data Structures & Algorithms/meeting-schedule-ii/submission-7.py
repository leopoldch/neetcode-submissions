"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = sorted(intervals, key=lambda x: x.start)
        ends = sorted(intervals, key= lambda x: x.end)
        nbRooms = 0
        last_end = 0

        for i in range(len(intervals)):
            starting = starts[i]

            if starting.start >= ends[last_end].end:
                last_end+=1
            else:
                nbRooms+=1
            
        return nbRooms
