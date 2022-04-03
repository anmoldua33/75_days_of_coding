from collections import *
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d=dict(Counter(nums))
        k=[]
        for i,j in d.items():
            if j>=2:
                k.append(i)
        return k
