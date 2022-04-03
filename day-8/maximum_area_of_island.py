class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        
        def dfs(i,j):
            nonlocal temp
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
                return
            grid[i][j]=0
            temp+=1
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        
        m=len(grid)
        n=len(grid[0])
        res=0
        
        for i in range(m):
            for j in range(n):
                temp=0
                if grid[i][j]==1:
                    dfs(i,j)
                    res=max(res,temp)
        return res
