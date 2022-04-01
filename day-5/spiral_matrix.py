class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left, right,  top, bottom = 0, COLS - 1, 0, ROWS - 1

        res:List[int] = []
        while left < right + 1 and top < bottom + 1:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top +=1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -=1

            if not (left < right + 1 and top < bottom + 1):
                break

            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -=1

            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left +=1

        return res
