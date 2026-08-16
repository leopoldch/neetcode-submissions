from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        steps_per_car = defaultdict(float)

        for local_position, local_speed in zip(position, speed):
            distance = target - local_position
            steps = distance / local_speed
            steps_per_car[local_position] = steps

        sorted_positions  = sorted(position)[::-1]
        total = 1 # at least one float 
        bottleneck = steps_per_car[sorted_positions[0]]

        for pos in sorted_positions:
            # at least 
            steps_c = steps_per_car[pos]
            if steps_c > bottleneck:
                total+=1
                bottleneck = steps_c

        
        return total