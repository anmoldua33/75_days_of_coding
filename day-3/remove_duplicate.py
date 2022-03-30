class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        co=0
        for i in range(len(nums)):
            if i>0:
                if nums[i]!=nums[i-1]:
                    co+=1
                nums[co]=nums[i]
        return co+1
