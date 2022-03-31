class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        acc = 0
        
        dic = defaultdict(int)
        dic[0] = 1 # 0 must to be counted
        
        for i in range(len(nums)):
            acc += nums[i]
            if acc-k in dic: count += dic[acc-k]
            
            dic[acc] += 1
        return count
