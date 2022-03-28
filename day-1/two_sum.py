class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    k.append(i)
                    k.append(j)

        return (k)

