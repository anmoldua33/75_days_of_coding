class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k=[]
        n=nums
        comb=permutations(nums,len(nums))
        for i in comb:
            p=list(i)
            k.append(i)
        k=sorted(set(k))
        e=[]
        for i in range(len(k)):
            w=list(k[i])
            e.append(w)
        for i in range(len(e)):
            if e[i]==n:
                p=(e[i+1])
                nums=p
                return nums
            
        """
        Do not return anything, modify nums in-place instead.
        """
        
