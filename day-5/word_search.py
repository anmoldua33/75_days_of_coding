class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i, j, ptr):
            if ptr == len(word):
                return True
            if i < 0 or j < 0 or i == m or j == n or board[i][j] == "-":
                return False
            
            if board[i][j] == word[ptr]:
                curr = board[i][j]
                board[i][j] = "-"
                
                top = dfs(i-1, j, ptr + 1)
                bottom = dfs(i+1, j, ptr + 1)
                right = dfs(i, j+1, ptr + 1)
                left = dfs(i, j-1, ptr + 1)
                
                board[i][j] = curr
                
                return top or bottom or right or left
            
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
