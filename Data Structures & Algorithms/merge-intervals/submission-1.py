class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)

        non_overlapping_intervals: List[List[int]] = [intervals[0]]

        for interval in intervals[1:]:
            last_interval = non_overlapping_intervals[-1]
            last_x = last_interval[0]
            last_y = last_interval[1]
            x = interval[0]; y = interval[1]

            if x > last_y:
                non_overlapping_intervals.append(interval)
                continue

            new_interval = [min(x, last_x), max(y, last_y)]
            non_overlapping_intervals[-1] = new_interval
            
        return non_overlapping_intervals