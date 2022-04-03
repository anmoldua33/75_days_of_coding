def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, count = len(nums), 0
		
        for i in range(n-1):
            if i>0 and nums[i] == nums[i-1]: continue
                
            l, r = i+1, n-1            
            while l<=r:
                mid = l+(r-l)//2
                if nums[mid]-nums[i] == k:
                    count += 1
                    break
                if nums[mid]-nums[i] > k:
                    r = mid-1
                else:
                    l = mid+1
        return count
