class Solution:
    def jump(self, nums: List[int]) -> int:
                
        max_reachable = 0
        nb_jumps = 0
        prev_max_reachable = 0

        for i, num in enumerate(nums):

            cur_jump = i+num
            max_reachable = max(max_reachable, cur_jump)

            if i>=prev_max_reachable and i != len(nums)-1:
                nb_jumps+=1
                prev_max_reachable = max_reachable
                
                    
        return nb_jumps


            


        