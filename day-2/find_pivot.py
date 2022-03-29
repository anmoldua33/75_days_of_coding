class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l = len(nums)
        n = 0
        for  i in range(0, l):
            if i > 0:
                n += nums[i-1]
                total -= nums[i]
            else:
                n += 0
                total -= nums[i]
                
            if n==total:
                return i

            i+=1
        
        return -1
