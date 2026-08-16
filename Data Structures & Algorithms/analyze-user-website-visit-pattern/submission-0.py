from collections import defaultdict, deque

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        values = sorted(zip(username, timestamp, website), key=lambda x: x[1])
        max_val = float("-inf")
        pattern = None
        patterns = defaultdict(int)
        current_pattern = defaultdict(deque)

        for username_i, timestamp_i, website_i in values:
            current_pattern[username_i].append(website_i)
            if len(current_pattern[username_i]) > 3:
                current_pattern[username_i].popleft()
            
            if len(current_pattern[username_i]) ==3:
                pattern_tuple = tuple(current_pattern[username_i])
                patterns[pattern_tuple] +=1
                if patterns[pattern_tuple] > max_val:
                    max_val = patterns[pattern_tuple]
                    pattern = pattern_tuple
        


        return list(pattern)
