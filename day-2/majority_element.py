class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        p={}
        l=[]
        p=dict(Counter(nums))
        for i,j in p.items():
            l.append(j)
        m=max(l)
        for i ,j in p.items():
            if j==m:
                return i
        
        
