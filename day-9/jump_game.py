class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for idx, steps in enumerate(nums):
            if idx > max_index:
                return False
            max_index = max(max_index, idx+steps)
        return True
