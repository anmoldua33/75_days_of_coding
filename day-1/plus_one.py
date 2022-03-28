class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        f=len(digits)
        s=0
        for i in range(f):
            s=s+(digits[i]*(10**(f-i-1)))
        s=s+1
        s=str(s)
        l=[]
        for i in range(len(s)):
            l.append(int(s[i]))
        return(l)

            
        
        
