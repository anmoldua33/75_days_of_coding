class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        list_combination = []
        li=[]
        for i in range(len(nums) + 1):
            list_combination += list(combinations(nums, i))
        for i in range(1,len(list_combination)):
            u=sum(list_combination[i])
            if u==target:
                print(list_combination[i])
        
