class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        hc=[0]+horizontalCuts+[h]
        vc=[0]+verticalCuts+[w]
        
        max1=-1
        max2=-1
        hc.sort()
        vc.sort()
        
        for i in range(1,len(hc)):
            max1=max(max1,hc[i]-hc[i-1])
        
        for i in range(1,len(vc)):
            max2=max(max2,vc[i]-vc[i-1])
        return (max1*max2)%(10**9+7)
            
            
