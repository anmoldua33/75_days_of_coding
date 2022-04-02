class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: 
            return 0
        
        curr = 0
        curr_farthest = curr+nums[0]
        jumps = 1
        
        while curr_farthest < len(nums) - 1:
            next_farthest_jump = -math.inf
            for i in range(curr+1, curr_farthest+1):
                if i+nums[i] > next_farthest_jump:
                    next_farthest_jump = max(next_farthest_jump, i+nums[i])
                    curr = i
            jumps += 1
            curr_farthest = next_farthest_jump
            
        return jumps
