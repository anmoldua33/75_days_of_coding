from itertools import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s=[]
        comb=permutations(nums,4)
        for i in comb:
            if sum(i)==target:
                s.append(list(i))
        return (s)
