class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)
        nbToRemove = 0
        last = intervals[0]

        for i in range(1, len(intervals)):
            current = intervals[i]

            if current[0] < last[1]:
                # overlap
                nbToRemove+=1
                if current[1] >= last[1]:
                    continue # we keep the last
            
            last = current
    
        return nbToRemove
