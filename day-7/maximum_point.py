class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = k
        total = 0
        
        lst_left = cardPoints[0:k]
        lst_right = cardPoints[-k:]
        
        sub_total = sum_left = sum(lst_left)
        sum_right = sum(lst_right)
        
        
        total = 0
        
        for i in range(k):
            sub_total = sub_total - lst_left.pop() + lst_right.pop()
            if sub_total > total:
                total = sub_total
        
        
        return max(sum_left,sum_right,total)
