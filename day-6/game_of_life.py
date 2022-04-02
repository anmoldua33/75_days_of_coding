class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        l = len(board[0])
        cur_lst = [0] * l
        prev_lst = []
        
        def write_result(board, lst, row):
            for j in range(l):
                board[row][j] = lst[j]
                
        def check_cell(row, col):
            if row < 0 or row >= h or col < 0 or col >= l:
                return 0
            return board[row][col]
        
        for i in range(h):
            for j in range(l):
                ns = 0
                for m in range(i-1,i+2):
                    for n in range(j-1, j+2):
                        if m == i and n == j:
                            continue
                        ns += check_cell(m,n)
                if board[i][j] == 1 and 1 < ns < 4: 
                    cur_lst[j] = 1
                elif board[i][j] == 0 and ns == 3:
                    cur_lst[j] = 1
                else:
                    cur_lst[j] = 0
                    
            if i > 0:
                write_result(board, prev_lst, i-1)
            
            prev_lst = cur_lst.copy()
        
        write_result(board, cur_lst, h-1)
