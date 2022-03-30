from collections import *
class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d={}
        nums.sort()
        l1=[]
        d=dict(Counter(nums))
        for i in d:
            a=i
            l=nums.index(a)+1
            h=len(nums)-1
            while l<h:
                if nums[l]+nums[h]==-a and [a,nums[l],nums[h]] not in l1:
                    l1.append([a,nums[l],nums[h]])
                    l+=1
                    h-=1
                elif (nums[l]+nums[h])>-a:
                    h-=1
                else:
                    l+=1
        return l1
